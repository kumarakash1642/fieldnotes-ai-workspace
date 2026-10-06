"""Local PDF extraction and reviewable, source-grounded company briefs."""
import hashlib
import io
import json
import re
from datetime import datetime
from uuid import uuid4
from pypdf import PdfReader

KINDS = ['Job description', 'Recruitment email', 'Other']
FACT_KINDS = ['company', 'role', 'responsibility', 'skill', 'eligibility', 'instruction', 'deadline', 'round']
ROUND_TYPES = ['Interview', 'GD', 'Case discussion', 'Assessment', 'Custom']
MAX_FILE = 5 * 1024 * 1024
MAX_PAGES = 30
MAX_TEXT = 60000

def upgrade_state(s):
    if not isinstance(s,dict) or not isinstance(s.get('processes'),list):
        return s
    for p in s['processes']:
        if not isinstance(p,dict): continue
        p.setdefault('documents', [])
        p.setdefault('brief', [])
        p.setdefault('proposal', {'items':[], 'source':'', 'message':'', 'fingerprint':''})
        for t in p.get('tasks',[]):
            if isinstance(t,dict): t.setdefault('requirementId','')
    return s

def extract_pdf(raw):
    if not raw or len(raw)>MAX_FILE: raise ValueError('Choose a PDF no larger than 5 MB.')
    if not raw.lstrip().startswith(b'%PDF-'): raise ValueError('This file is not a PDF.')
    try:
        reader=PdfReader(io.BytesIO(raw))
        if reader.is_encrypted: raise ValueError('Password-protected PDFs are not supported. Upload an unlocked copy.')
        if not 1 <= len(reader.pages) <= MAX_PAGES: raise ValueError('Use a PDF containing 1 to 30 pages.')
        pages=[];warnings=[];total=0
        for number,page in enumerate(reader.pages,1):
            try: text=(page.extract_text() or '').replace('\x00','').strip()
            except Exception: text='';warnings.append(f'Page {number} could not be read.')
            if len(text)<20: warnings.append(f'Page {number} has little or no readable text. Paste its text manually; scanned pages need OCR.')
            if len(text)>12000: warnings.append(f'Page {number} was truncated to 12,000 characters; check the original.')
            text=text[:12000]
            if total+len(text)>MAX_TEXT:
                warnings.append('Extraction reached the 60,000-character limit. Check remaining pages and add key details manually.')
                text=text[:max(0,MAX_TEXT-total)]
            total+=len(text);pages.append({'number':number,'text':text})
        return pages,list(dict.fromkeys(warnings))
    except ValueError:
        raise
    except Exception:
        raise ValueError('The PDF could not be read. Export a fresh PDF and try again.') from None

def fingerprint(p):
    value=[{'id':d['id'],'kind':d['kind'],'pages':d['pages']} for d in p['documents'] if d['included']]
    return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()

def source_page(p,item):
    doc=next((d for d in p['documents'] if d['id']==item['documentId']),None)
    page=next((pg for pg in doc['pages'] if pg['number']==item['page']),None) if doc else None
    return doc,page

def validate_documents(p,shape,string,listof,flag,integer,datevalue,identified):
    listof(p['documents'],12);identified(p['documents'])
    for d in p['documents']:
        shape(d,['id','name','kind','uploadedAt','sha256','pages','warnings','included'])
        string(d['name'],240);datevalue(d['uploadedAt']);flag(d['included'])
        if d['kind'] not in KINDS or not re.fullmatch(r'[a-f0-9]{64}',str(d['sha256'])): raise ValueError('Invalid PDF metadata.')
        listof(d['pages'],MAX_PAGES);listof(d['warnings'],100)
        if not d['pages']: raise ValueError('PDF page list is empty.')
        for i,pg in enumerate(d['pages'],1):
            shape(pg,['number','text']);integer(pg['number'],i,i);string(pg['text'],12000)
        if sum(len(pg['text']) for pg in d['pages'])>MAX_TEXT: raise ValueError('Document text exceeds 60,000 characters.')
        for warning in d['warnings']: string(warning,1000)
    shape(p['proposal'],['items','source','message','fingerprint'])
    for k in ['source','message','fingerprint']: string(p['proposal'][k])
    for collection in [p['proposal']['items'],p['brief']]:
        listof(collection,100);identified(collection)
        for item in collection:
            shape(item,['id','kind','text','date','roundType','documentId','page','quote','selected'])
            if item['kind'] not in FACT_KINDS or item['roundType'] not in ROUND_TYPES: raise ValueError('Unknown company brief field.')
            string(item['text'],2000);string(item['quote'],2000);flag(item['selected']);datevalue(item['date']);integer(item['page'],1,MAX_PAGES)
            doc,pg=source_page(p,item)
            if not pg: raise ValueError('Company brief references an unknown PDF page.')

def local_analysis(p):
    items=[]
    for d in p['documents']:
        if not d['included']: continue
        for pg in d['pages']:
            section='instruction'
            for line in pg['text'].splitlines():
                line=line.strip(' \t•-');low=line.lower()
                if len(line)<3: continue
                if re.fullmatch(r'(key )?(responsibilities|skills|requirements|eligibility|qualifications)\s*:?',low):
                    section={'responsibilities':'responsibility','skills':'skill','requirements':'skill','eligibility':'eligibility','qualifications':'eligibility'}.get(low.replace('key ','').rstrip(':'),'instruction');continue
                kind=section;value=line;date='';rtype='Custom'
                match=re.match(r'^(company|organisation|organization|role|job title|position)\s*:\s*(.+)',line,re.I)
                if match:kind='company' if match[1].lower() in ['company','organisation','organization'] else 'role';value=match[2]
                elif re.search(r'\b(deadline|apply by|register by|last date)\b',low):
                    kind='deadline'
                    # Never guess numeric day/month order, missing years or time zones.
                    dt=re.search(r'\b(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2})\b',line)
                    if dt and not re.search(r'\b(UTC|GMT|EST|PST|CET)\b',line):
                        try:date=datetime.fromisoformat(dt[1]+'T'+dt[2]).isoformat(timespec='minutes')
                        except ValueError:pass
                elif re.search(r'\b(round|interview|group discussion|assessment|selection process)\b',low):
                    kind='round';rtype='GD' if 'group discussion' in low else 'Case discussion' if 'case' in low else 'Interview' if 'interview' in low else 'Assessment' if 'assessment' in low or 'test' in low else 'Custom'
                elif any(x in low for x in ['excel','sql','power bi','required skill','proficiency']):kind='skill'
                elif any(x in low for x in ['eligible','cgpa','qualification']):kind='eligibility'
                if len(line)>2000:line=line[:2000];value=value[:2000]
                ident=hashlib.sha256(f"{d['id']}|{pg['number']}|{kind}|{line}".encode()).hexdigest()[:24]
                items.append(dict(id=ident,kind=kind,text=value,date=date,roundType=rtype,documentId=d['id'],page=pg['number'],quote=line,selected=False))
                if len(items)>=60:return items
    return items

def analysis_context(p):
    included=[d for d in p['documents'] if d['included']]
    if not included:raise ValueError('Upload and include at least one PDF first.')
    if not any(pg['text'].strip() for d in included for pg in d['pages']):raise ValueError('No readable text. Paste the PDF text into the page preview first.')
    # Bound the request explicitly. Never silently send only the first pages.
    if sum(len(pg['text']) for d in included for pg in d['pages'])>60000:
        raise ValueError('Selected text exceeds 60,000 characters. Exclude documents or shorten the editable text before analysis.')
    return {'documents':[{'id':d['id'],'kind':d['kind'],'pages':d['pages']} for d in included]}

def fact_schema():
    fields={'kind':{'type':'STRING','enum':FACT_KINDS},'text':{'type':'STRING'},'documentId':{'type':'STRING'},'page':{'type':'INTEGER'},'quote':{'type':'STRING'}}
    return {'type':'OBJECT','properties':{'items':{'type':'ARRAY','items':{'type':'OBJECT','properties':fields,'required':list(fields)}}},'required':['items']}

def validate_analysis(value,p):
    if not isinstance(value,dict) or set(value)!={'items'} or not isinstance(value['items'],list) or len(value['items'])>60:raise ValueError('Invalid document analysis format.')
    items=[]
    for v in value['items']:
        if not isinstance(v,dict) or set(v)!={'kind','text','documentId','page','quote'}:raise ValueError('Invalid document analysis field.')
        if v['kind'] not in FACT_KINDS or type(v['page']) is not int:raise ValueError('Invalid document analysis reference.')
        if any(not isinstance(v[k],str) or not v[k].strip() or len(v[k])>2000 for k in ['text','quote','documentId']):raise ValueError('Invalid document analysis text.')
        doc,pg=source_page(p,v)
        if not doc or not doc['included'] or not pg or ' '.join(v['quote'].split()) not in ' '.join(pg['text'].split()):
            raise ValueError('Document analysis included a quote not found on the cited page.')
        ident=hashlib.sha256(f"{v['documentId']}|{v['page']}|{v['kind']}|{v['quote']}".encode()).hexdigest()[:24]
        if any(x['id']==ident for x in items):continue
        # Dates/round type remain user-confirmed to avoid invented times or inferred rounds.
        items.append(dict(v,id=ident,date='',roundType='Custom',selected=False))
    return items

def apply_proposal(p):
    if p['proposal']['fingerprint']!=fingerprint(p):raise ValueError('Documents changed after analysis. Analyse them again before applying updates.')
    chosen=[x for x in p['proposal']['items'] if x['selected']]
    if not chosen:raise ValueError('Select at least one proposed detail to apply.')
    for kind in ['company','role','deadline']:
        fields=[x for x in chosen if x['kind']==kind]
        if len(fields)>1:raise ValueError(f'Conflicting {kind} entries: select one value or edit the proposals first.')
    for x in chosen:
        if not x['text'].strip():raise ValueError('Selected details must not be empty.')
        if x['kind']=='deadline' and not x['date']:raise ValueError('Enter the exact date and time for the selected deadline. Ambiguous dates are never guessed.')
    for x in chosen:
        kind=x['kind']
        if kind in ['company','role']:p[kind]=x['text']
        elif kind=='deadline':p['deadline']=x['date']
        elif kind=='round':
            # Existing round dates/statuses are never overwritten by a document update.
            rid='doc_'+x['id']
            if not any(r['id']==rid or r['name'].strip().lower()==x['text'].strip().lower() for r in p['rounds']):
                p['rounds'].append(dict(id=rid,name=x['text'][:200],type=x['roundType'],date=x['date'],status='Upcoming'))
        else:
            target='description' if kind in ['responsibility','skill','eligibility'] else 'details'
            if x['text'] not in p[target]:p[target]=(p[target]+'\n'+x['text']).strip()
        if kind in ['company','role','deadline']:
            for previous in p['brief']:
                if previous['kind']==kind:previous['selected']=False
        previous=next((z for z in p['brief'] if z['id']==x['id']),None)
        if previous:previous.update(x)
        else:p['brief'].append(dict(x))
    return len(chosen)

def requirement_tasks(p):
    tasks=[]
    mappings=[('excel','a1'),('sql','a2'),('power bi','a4'),('market','m2'),('customer','s4'),('distributor','s4'),('sales','s4'),('operation','l1'),('data','a5'),('leadership','o4')]
    for item in p['brief']:
        if not item['selected'] or item['kind'] not in ['skill','responsibility','eligibility','instruction']:continue
        low=item['text'].lower();qid=next((q for word,q in mappings if word in low),'p5')
        title=('Check eligibility: ' if item['kind']=='eligibility' else 'Prepare: ')+item['text'][:150]
        doc,_=source_page(p,item)
        tasks.append(dict(title=title,reason=f"From {doc['name']}, page {item['page']}: {item['text'][:900]}. Prepare evidence or a worked example; do not claim experience you cannot demonstrate.",priority='High',minutes=25,questionId=qid,requirementId=item['id']))
    return tasks
