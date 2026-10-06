import io
import json
import re
import sqlite3
import tempfile
import unittest
import zipfile
from contextlib import closing
from pathlib import Path
from unittest.mock import patch
from pypdf import PdfWriter
from pypdf.generic import NameObject, DictionaryObject, DecodedStreamObject
from app import create_app, generation_context
from company_documents import validate_analysis, fingerprint


def pdf_bytes(lines=None,encrypted=False,pages=1):
    writer=PdfWriter()
    for n in range(pages):
        page=writer.add_blank_page(width=612,height=792)
        if lines:
            font=DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/Type1'),NameObject('/BaseFont'):NameObject('/Helvetica')})
            page[NameObject('/Resources')]=DictionaryObject({NameObject('/Font'):DictionaryObject({NameObject('/F1'):writer._add_object(font)})})
            stream=DecodedStreamObject()
            operations=['BT /F1 12 Tf 40 740 Td']
            for line in lines:
                safe=line.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
                operations.append('('+safe+') Tj 0 -20 Td')
            operations.append('ET');stream.set_data('\n'.join(operations).encode('ascii'))
            page[NameObject('/Contents')]=writer._add_object(stream)
    if encrypted:writer.encrypt('private')
    out=io.BytesIO();writer.write(out);return out.getvalue()


class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'db.sqlite3';self.app=create_app(self.path);self.client=self.app.test_client()
        self.token=re.search('name="workspace-token" content="([^"]+)"',self.client.get('/').get_data(as_text=True)).group(1)
        self.headers={'X-Workspace-Token':self.token}
        b=self.get();b['state']['processes']=[dict(id='p1',company='My company',role='My edited role',description='Manual JD note',details='My process note',deadline='2026-11-01T12:00',rounds=[dict(id='r1',name='Interview',type='Interview',date='2026-11-02T12:00',status='Upcoming')],tasks=[])]
        self.save(b)

    def tearDown(self):self.tmp.cleanup()
    def get(self):return self.client.get('/api/bootstrap').get_json()
    def save(self,b):
        r=self.client.put('/api/state',json={'state':b['state'],'version':b['version']},headers=self.headers);self.assertEqual(r.status_code,200,r.get_json());return r
    def post(self,path,**fields):return self.client.post(path,json={'processId':'p1','version':self.get()['version'],**fields},headers=self.headers)
    def upload(self,raw=None,name='job.pdf',kind='Job description'):
        if raw is None:raw=pdf_bytes(['Company: ExampleCo','Role: Sales Intern','Skills:','Excel reporting','Customer discovery','Responsibilities:','Manage distributor relationships','Deadline: 2026-10-12 17:00'])
        return self.client.post('/api/documents/upload',data={'version':str(self.get()['version']),'processId':'p1','kind':kind,'file':(io.BytesIO(raw),name)},headers=self.headers)
    def prepare(self):
        self.assertEqual(self.upload().status_code,200)
        r=self.post('/api/documents/analyse',mode='local');self.assertEqual(r.status_code,200,r.get_json());return self.get()

    def test_upload_local_no_auto_analysis_and_duplicate_preserves_edits(self):
        with patch('app.request_gemini') as ai:
            r=self.upload();self.assertEqual(r.status_code,200);ai.assert_not_called()
        b=self.get();p=b['state']['processes'][0];d=p['documents'][0]
        self.assertIn('Excel reporting',d['pages'][0]['text']);self.assertEqual(p['role'],'My edited role');self.assertFalse(p['proposal']['items'])
        d['pages'][0]['text']='Edited extraction';self.save(b)
        self.assertEqual(self.upload().status_code,200)
        p=self.get()['state']['processes'][0];self.assertEqual(len(p['documents']),1);self.assertEqual(p['documents'][0]['pages'][0]['text'],'Edited extraction')

    def test_bad_scanned_encrypted_large_and_stale_uploads(self):
        for raw,name in [(b'not a pdf','bad.pdf'),(pdf_bytes(encrypted=True),'locked.pdf'),(b'%PDF-'+b'x'*(5*1024*1024),'large.pdf'),(pdf_bytes(pages=31),'long.pdf'),(pdf_bytes(),'wrong.txt')]:
            self.assertEqual(self.upload(raw,name).status_code,400)
        r=self.upload(pdf_bytes());self.assertEqual(r.status_code,200);d=r.get_json()['state']['processes'][0]['documents'][0];self.assertTrue(d['warnings'])
        self.assertEqual(self.post('/api/documents/analyse',mode='local').status_code,400)
        b=self.get();b['state']['processes'][0]['documents'][0]['pages'][0]['text']='Skills:\nExcel reporting';self.save(b)
        self.assertEqual(self.post('/api/documents/analyse',mode='local').status_code,200)

    def test_review_apply_conflict_and_preservation(self):
        b=self.prepare();p=b['state']['processes'][0]
        self.assertEqual(p['role'],'My edited role')
        for item in p['proposal']['items']:
            if item['kind'] in ['role','skill','responsibility']:item['selected']=True
        self.save(b);r=self.post('/api/documents/apply');self.assertEqual(r.status_code,200,r.get_json());p=r.get_json()['state']['processes'][0]
        self.assertEqual(p['role'],'Sales Intern');self.assertIn('Manual JD note',p['description']);self.assertEqual(p['deadline'],'2026-11-01T12:00')
        self.assertEqual(p['rounds'][0]['date'],'2026-11-02T12:00')
        self.assertTrue(p['brief'])

    def test_conflicting_deadlines_and_changed_extraction(self):
        self.upload(pdf_bytes(['Deadline: 2026-10-12 17:00','Deadline: 2026-10-13 18:00']))
        self.post('/api/documents/analyse',mode='local');b=self.get()
        for item in b['state']['processes'][0]['proposal']['items']:item['selected']=True
        self.save(b);self.assertEqual(self.post('/api/documents/apply').status_code,400)
        b=self.get();p=b['state']['processes'][0];p['proposal']['items'][1]['selected']=False;p['documents'][0]['pages'][0]['text']+='\nChanged notice';self.save(b)
        r=self.post('/api/documents/apply');self.assertEqual(r.status_code,400);self.assertIn('changed after analysis',r.get_json()['error'])

    def test_same_answer_different_requirements_are_separate(self):
        b=self.prepare();p=b['state']['processes'][0]
        for item in p['proposal']['items']:item['selected']=item['kind'] in ['skill','responsibility']
        self.save(b);self.post('/api/documents/apply')
        r=self.post('/api/generate',roundId='r1',mode='local');self.assertEqual(r.status_code,200,r.get_json())
        b=self.get();p=b['state']['processes'][0];linked=[t for t in p['tasks'] if t['requirementId']]
        self.assertEqual(len([t for t in linked if t['questionId']=='s4']),2)
        p['tasks'][0]['done']=True;p['tasks'][0]['title']='My edited prep task';self.save(b)
        r=self.post('/api/generate',roundId='r1',mode='local').get_json();self.assertEqual(r['added'],0);self.assertTrue(r['state']['processes'][0]['tasks'][0]['done'])
        self.assertEqual(r['state']['processes'][0]['tasks'][0]['title'],'My edited prep task')

    def test_ai_failure_falls_back_and_quotes_must_exist(self):
        b=self.prepare();p=b['state']['processes'][0];d=p['documents'][0]
        b['state']['settings']={'aiConsent':True,'freeTierConfirmed':True};self.save(b)
        with patch('app.env_config',return_value={'GEMINI_API_KEY':'secret','GEMINI_MODEL':'gemini-test'}),patch('app.request_gemini',side_effect=OSError()):
            r=self.post('/api/documents/analyse',mode='gemini');self.assertEqual(r.status_code,200);self.assertEqual(r.get_json()['state']['processes'][0]['proposal']['source'],'Local extraction')
        bad={'items':[{'kind':'round','text':'Guaranteed interview','documentId':d['id'],'page':1,'quote':'A sentence not in the document'}]}
        with self.assertRaises(ValueError):validate_analysis(bad,p)
        good={'items':[{'kind':'skill','text':'Excel reporting','documentId':d['id'],'page':1,'quote':'Excel reporting'}]}
        self.assertEqual(validate_analysis(good,p)[0]['selected'],False)

    def test_json_and_original_archive_restore(self):
        self.prepare();backup=self.client.get('/api/backup').get_json();self.assertEqual(backup['schemaVersion'],2)
        z=self.client.get('/api/documents/archive');self.assertEqual(z.status_code,200)
        with zipfile.ZipFile(io.BytesIO(z.data)) as archive:self.assertTrue(any(n.endswith('.pdf') for n in archive.namelist()))
        with closing(sqlite3.connect(self.path)) as c:
            c.execute('DELETE FROM pdf_files');c.commit()
        r=self.client.post('/api/restore',json={'backup':backup,'version':self.get()['version']},headers=self.headers);self.assertEqual(r.status_code,200)
        d=self.get()['state']['processes'][0]['documents'][0];url=f"/api/documents/p1/{d['id']}/download"
        self.assertEqual(self.client.get(url).status_code,404)
        r=self.client.post('/api/documents/archive',data={'file':(io.BytesIO(z.data),'originals.zip')},headers=self.headers);self.assertEqual(r.status_code,200,r.get_json())
        self.assertTrue(self.client.get(url).data.startswith(b'%PDF-'))

    def test_legacy_workspace_upgrade_and_backup(self):
        b=self.get();p=b['state']['processes'][0]
        for k in ['documents','brief','proposal']:p.pop(k)
        with closing(sqlite3.connect(self.path)) as c:
            c.execute('UPDATE workspace SET body=?',(json.dumps(b['state']),));c.commit()
        newer=create_app(self.path).test_client().get('/api/bootstrap').get_json()
        self.assertEqual(newer['state']['processes'][0]['documents'],[])
        self.assertEqual(newer['state']['processes'][0]['role'],'My edited role')
        self.assertTrue(list(Path(self.tmp.name).glob('before-documents-upgrade-*.sqlite3')))

    def test_preview_approved_context_only_and_source_escape(self):
        self.upload(pdf_bytes(['Email: private@example.com','Skills:','Excel reporting']))
        preview=self.post('/api/documents/context').get_json();self.assertNotIn('private@example.com',json.dumps(preview));self.assertIn('[email removed]',json.dumps(preview))
        b=self.get();p=b['state']['processes'][0];context=generation_context(b['state'],p,p['rounds'][0])
        self.assertEqual(context['approvedRequirements'],[]);self.assertNotIn('documents',context)

if __name__=='__main__':unittest.main()
