import copy
import json
import re
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

from app import create_app, generation_context, validate_suggestions, parse_gemini_response, gemini_failure_message, GeminiResponseError
from seed import QUESTIONS, initial_state


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=Path(self.tmp.name)/'test.sqlite3'
        self.app=create_app(self.path)
        self.client=self.app.test_client()
        html=self.client.get('/').get_data(as_text=True)
        self.token=re.search(r'name="workspace-token" content="([^"]+)"',html).group(1)
        self.headers={'X-Workspace-Token':self.token}

    def tearDown(self): self.tmp.cleanup()

    def snapshot(self):
        data=self.client.get('/api/bootstrap').get_json()
        return data['state'],data['version']

    def save(self,s,v): return self.client.put('/api/state',json={'state':s,'version':v},headers=self.headers)

    def company(self,ai=False):
        s,v=self.snapshot()
        s['settings']={'aiConsent':ai,'freeTierConfirmed':ai}
        s['processes']=[dict(id='company1',company='Example Company',role='Sales and Marketing Intern',description='Customer research and analysis',details='GD followed by interview',deadline='',rounds=[dict(id='round1',name='GD',type='GD',date='2026-10-10T10:00',status='Upcoming')],tasks=[])]
        self.assertEqual(self.save(s,v).status_code,200)

    def generate(self,mode='local'):
        _,v=self.snapshot()
        return self.client.post('/api/generate',json={'processId':'company1','roundId':'round1','version':v,'mode':mode},headers=self.headers)

    def test_seed_coverage_and_drafts(self):
        self.assertEqual(len(QUESTIONS),44)
        self.assertEqual(len({q['id'] for q in QUESTIONS}),44)
        self.assertEqual(len(QUESTIONS[0]['frames']),9)
        for q in QUESTIONS:
            self.assertTrue(all(len(v)>30 for v in q['frames'].values()),q['id'])
            self.assertGreaterEqual(len(q['adaptations']),2)
            self.assertTrue(q['evidence'] and q['improve'] and q['follow'])

    def test_edit_persistence_history_and_conflict(self):
        s,v=self.snapshot();label=next(iter(s['answers']['p1']['frames']))
        original=s['answers']['p1']['frames'][label]
        s['answers']['p1']['frames'][label]='My genuine revised introduction.'
        self.assertEqual(self.save(s,v).status_code,200)
        self.assertEqual(self.save(s,v).status_code,409)
        other=create_app(self.path).test_client().get('/api/bootstrap').get_json()
        self.assertEqual(other['state']['answers']['p1']['frames'][label],s['answers']['p1']['frames'][label])
        history=self.client.get('/api/revisions/p1').get_json()['revisions']
        self.assertEqual(history[0]['frames'][label],original)

    def test_local_generation_dedup_preserves_work(self):
        self.company();first=self.generate().get_json();self.assertGreater(first['added'],0)
        s,v=self.snapshot();p=s['processes'][0];p['tasks'][0]['done']=True;p['tasks'][0]['title']='My edited task'
        s['reviews'].append(dict(id='review1',processId=p['id'],roundId='round1',date='2026-10-01T09:00',questions='Q',response='R',worked='W',weakness='Need evidence',feedback='Be specific',outcome='Pending',tags=['Evidence']))
        self.save(s,v);second=self.generate().get_json()
        self.assertTrue(second['state']['processes'][0]['tasks'][0]['done'])
        self.assertEqual(second['state']['processes'][0]['tasks'][0]['title'],'My edited task')
        self.assertEqual(second['state']['reviews'][0]['response'],'R')
        self.assertEqual(second['added'],1) # New review weakness task only.
        third=self.generate().get_json();self.assertEqual(third['added'],0)
        self.assertEqual(len(third['state']['generations']),3)

    def test_backup_restore_history_and_no_key(self):
        s,v=self.snapshot();s['answers']['p2']['notes']='A saved note';s['answers']['p2']['frames']['60-second walkthrough']='Revised';self.save(s,v)
        with patch('app.env_config',return_value={'GEMINI_API_KEY':'SUPER_SECRET','GEMINI_MODEL':'gemini-3.8-flash'}):
            self.assertNotIn('SUPER_SECRET',self.client.get('/api/bootstrap').get_data(as_text=True))
            result=self.client.get('/api/backup');self.assertNotIn('SUPER_SECRET',result.get_data(as_text=True));b=result.get_json()
        s,v=self.snapshot();s['answers']['p2']['notes']='Changed';self.save(s,v)
        _,v=self.snapshot();result=self.client.post('/api/restore',json={'backup':b,'version':v},headers=self.headers)
        self.assertEqual(result.status_code,200,result.get_json())
        self.assertEqual(result.get_json()['state']['answers']['p2']['notes'],'A saved note')
        self.assertFalse(result.get_json()['state']['settings']['aiConsent'])
        self.assertTrue(list(Path(self.tmp.name).glob('before-restore-*.sqlite3')))
        self.assertTrue(self.client.get('/api/revisions/p2').get_json()['revisions'])

    def test_invalid_state_and_backup_leave_data_intact(self):
        before,v=self.snapshot();bad=copy.deepcopy(before);bad['answers']['p1']['confidence']=10
        self.assertEqual(self.save(bad,v).status_code,400)
        b=self.client.get('/api/backup').get_json();b['state']['processes']=[{'id':'invalid'}]
        self.assertEqual(self.client.post('/api/restore',json={'backup':b,'version':v},headers=self.headers).status_code,400)
        self.assertEqual(self.snapshot(),(before,v))

    def test_write_token_and_host(self):
        s,v=self.snapshot();self.assertEqual(self.client.put('/api/state',json={'state':s,'version':v}).status_code,403)
        self.assertEqual(self.client.get('/api/bootstrap',headers={'Host':'evil.example'}).status_code,403)

    def test_ai_consent_is_required(self):
        self.company();self.assertEqual(self.generate('gemini').status_code,400)

    def test_missing_key_falls_back(self):
        self.company(ai=True)
        with patch('app.env_config',return_value={'GEMINI_API_KEY':'','GEMINI_MODEL':'gemini-3.8-flash'}):
            r=self.generate('gemini').get_json()
        self.assertEqual(r['source'],'Local rules');self.assertIn('No Gemini key',r['message'])

    def test_ai_errors_fall_back_without_overwriting_reviews(self):
        self.company(ai=True)
        failures=[urllib.error.HTTPError('url',429,'quota',{},None),OSError('offline'),ValueError('invalid JSON')]
        for error in failures:
            with patch('app.env_config',return_value={'GEMINI_API_KEY':'test','GEMINI_MODEL':'gemini-3.8-flash'}),patch('app.gemini_tasks',side_effect=error):
                response=self.generate('gemini');self.assertEqual(response.status_code,200,response.get_json());self.assertEqual(response.get_json()['source'],'Local rules')

    def test_valid_ai_tasks_and_payload_minimisation(self):
        self.company(ai=True);s,v=self.snapshot();s['processes'][0]['details']='Contact Demo Candidate at person@example.com or 9876543210';self.save(s,v)
        tasks=[dict(title='Practise a concise introduction',reason='Role alignment',priority='High',minutes=20,questionId='p1')]
        with patch('app.env_config',return_value={'GEMINI_API_KEY':'test','GEMINI_MODEL':'gemini-3.8-flash'}),patch('app.gemini_tasks',return_value=tasks) as generate:
            r=self.generate('gemini').get_json();context=generate.call_args.args[0]
        self.assertEqual(r['source'],'Gemini');self.assertEqual(r['added'],1)
        encoded=json.dumps(context)
        for text in ['person@example.com','9876543210','Demo Candidate','frames','GEMINI_API_KEY']:self.assertNotIn(text,encoded)

    def test_invalid_ai_schema(self):
        for value in [{}, {'tasks':[]}, {'tasks':[dict(title='x',reason='x',priority='High',minutes=-5,questionId='bad')]}]:
            with self.assertRaises(ValueError): validate_suggestions(value)

    def test_completed_round_does_not_generate(self):
        self.company();s,v=self.snapshot();s['processes'][0]['rounds'][0]['status']='Completed';self.save(s,v)
        self.assertEqual(self.generate().status_code,400)

    def test_gemini_errors_are_distinct_and_safe(self):
        denied=urllib.error.URLError(PermissionError(13,'hidden details'))
        self.assertIn('Windows blocked',gemini_failure_message(denied))
        self.assertIn('35 seconds',gemini_failure_message(TimeoutError()))
        self.assertIn('503',gemini_failure_message(urllib.error.HTTPError('secret-url',503,'private body',{},None)))
        self.assertNotIn('secret',gemini_failure_message(urllib.error.HTTPError('secret-url',503,'private body',{},None)))
        self.assertIn('429',gemini_failure_message(urllib.error.HTTPError('url',429,'',{},None)))

    def test_gemini_response_parser(self):
        task=dict(title='Practise introduction',reason='Keep it relevant',priority='High',minutes=20,questionId='p1')
        payload={'candidates':[{'finishReason':'STOP','content':{'parts':[{'thought':True,'text':'not returned'},{'text':json.dumps({'tasks':[task]})}]}}]}
        self.assertEqual(parse_gemini_response(payload),[dict(task,requirementId='')])
        examples=[({},'no answer'),({'candidates':[]},'no answer'),({'promptFeedback':{'blockReason':'SAFETY'}},'blocked'),({'candidates':[{'finishReason':'MAX_TOKENS'}]},'response limit'),({'candidates':[{'finishReason':'STOP','content':{'parts':[{'text':'truncated JSON'}]}}]},'required format')]
        for body,expected in examples:
            with self.assertRaisesRegex(GeminiResponseError,expected):parse_gemini_response(body)

    def test_network_permission_fallback_explains_zero_new_tasks(self):
        self.company(ai=True);self.generate()
        with patch('app.env_config',return_value={'GEMINI_API_KEY':'test','GEMINI_MODEL':'gemini-3.8-flash'}),patch('app.gemini_tasks',side_effect=urllib.error.URLError(PermissionError(13,'blocked'))):
            response=self.generate('gemini').get_json()
        self.assertEqual(response['added'],0)
        self.assertIn('Windows blocked',response['message'])
        self.assertIn('matching preparation tasks already exist',response['message'])

if __name__=='__main__': unittest.main()
