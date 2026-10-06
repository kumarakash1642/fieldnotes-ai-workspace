'use strict';
function ensureDocuments(p){p.documents??=[];p.brief??=[];p.proposal??={items:[],source:'',message:'',fingerprint:''};}
function documentSource(p,item){const d=p.documents.find(d=>d.id===item.documentId);return `${d?.name||'Document'} · page ${item.page}`;}
function sourceButton(p,item){return button(E(documentSource(p,item)),'doc-source','quiet',`data-document="${E(item.documentId)}" data-page="${item.page}"`);}
function documentsPanel(p){
 ensureDocuments(p);const pi=state.processes.indexOf(p),base=`processes.${pi}`;
 return `<section class="card document-panel"><div class="card-head"><div><div class="eyebrow">FROM THE ACTUAL OPPORTUNITY</div><h2>JD & recruitment documents</h2></div>${pill(p.documents.length+' / 12 PDFs','cyan')}</div>
 <p class="muted">Upload a job description or a recruitment email saved as PDF. Text extraction stays local; uploading does not call Gemini.</p><br>
 <div class="form-grid"><label class="field"><span>Document type</span><select id="doc-kind">${['Job description','Recruitment email','Other'].map(k=>`<option>${E(k)}</option>`).join('')}</select></label><label class="field"><span>Choose PDFs</span><input id="doc-files" type="file" accept="application/pdf,.pdf" multiple><small>Up to 5 MB and 30 pages per PDF. Text-based PDFs; no automatic OCR.</small></label></div>
 ${button('↑ Upload PDFs','doc-upload','secondary')}
 <div class="document-list">${p.documents.map((d,di)=>`<details class="document-item"><summary><span>${E(d.name)}</span> ${pill(d.kind,'neutral')} ${d.warnings.length?pill('CHECK EXTRACTION','orange'):pill(d.pages.length+' PAGES','cyan')}</summary><div class="document-body"><p class="rubric">Uploaded ${E(dateLabel(d.uploadedAt))} · Original remains unchanged when you edit the text below.</p><label class="check-label"><input type="checkbox" ${bind(`${base}.documents.${di}.included`)} ${d.included?'checked':''}>Include in the next analysis</label><a href="/api/documents/${encodeURIComponent(p.id)}/${encodeURIComponent(d.id)}/download" download>↓ Download original PDF</a>${d.warnings.map(w=>`<p class="doc-warning">${E(w)}</p>`).join('')}${d.pages.map((pg,pgidx)=>area('Page '+pg.number+' — extracted text (editable)',`${base}.documents.${di}.pages.${pgidx}.text`,5)).join('')}</div></details>`).join('')}</div>
 ${p.documents.length?`<div class="analysis-controls"><label class="field"><span>Document analysis method</span><select id="doc-mode"><option value="local">Local extraction · always free</option value="gemini">Gemini · uses your API quota</option></select></label>${button('Analyse documents','doc-analyse','primary')}${button('Preview text sent to AI','doc-preview','quiet')}</div><p class="rubric">Local extraction finds candidate details; it does not fully understand the document. Review all proposed fields. Gemini sends only the included text, after basic redaction, when explicitly selected.</p>`:''}
 </section>${proposalPanel(p,base)}${approvedPanel(p,base)}`;
}
function proposalPanel(p,base){
 const proposal=p.proposal;if(!proposal.source)return '';
 const existing={company:p.company,role:p.role,deadline:p.deadline};
 const conflictKinds=['company','role','deadline'].filter(k=>new Set(proposal.items.filter(i=>i.kind===k).map(i=>i.text.trim().toLowerCase())).size>1);
 return `<section class="card"><div class="card-head"><h2>Review proposed updates</h2>${pill(proposal.source,'cyan')}</div><p class="muted">${E(proposal.message)}</p><p class="doc-warning">Only checked details will be applied. Company, role and deadline selections replace their existing value; other details append. Existing round dates and completed work stay unchanged.</p>${conflictKinds.length?`<p class="doc-warning"><strong>Conflicting candidates:</strong> ${E(conflictKinds.join(', '))}. Check the source documents and select only one value for each.</p>`:''}
 <p class="rubric">Dates and times are entered in your computer’s local time zone. A date without a time, an ambiguous date or a time in another zone needs manual confirmation.</p>
 ${proposal.items.map((item,i)=>{const path=`${base}.proposal.items.${i}`;return `<details class="proposal-item"><summary><span>${E(item.kind.toUpperCase())} · ${E(item.text.slice(0,130))}</span></summary><div class="document-body"><label class="check-label"><input type="checkbox" ${bind(path+'.selected')} ${item.selected?'checked':''}>Apply this detail</label><div class="form-grid">${select('Detail type',path+'.kind',data.factKinds||['company','role','responsibility','skill','eligibility','instruction','deadline','round'])}<div class="span-2">${area('Proposed value — edit before applying',path+'.text',2)}</div>${input('Date and time — required only for a deadline',path+'.date','datetime-local')}${select('Round type — used only for a round',path+'.roundType',data.roundTypes)}</div>${item.kind in existing?`<p class="doc-warning">Current ${E(item.kind)}: ${E(existing[item.kind]||'Not set')}. Applying replaces this value.</p>`:''}<blockquote>${E(item.quote)}</blockquote>${sourceButton(p,item)}<p class="rubric">The quote is evidence from the extracted text. Your edited summary may differ; verify it before applying.</p></div></details>`;}).join('')||empty('No details found','Edit the extracted text or add the job description manually.')}
 <br>${button('Apply selected updates','doc-apply','primary')}
 </section>`;
}
function approvedPanel(p,base){
 if(!p.brief.length)return '';
 return `<section class="card"><div class="card-head"><h2>Approved company brief</h2>${pill('USED FOR PREPARATION')}</div><p class="muted">These are your reviewed facts, not suggested interview rounds. Uncheck an outdated requirement to exclude it from future task generation. Existing tasks remain in your checklist.</p>${p.brief.map((item,i)=>`<div class="approved-item"><label class="check-label"><input type="checkbox" ${bind(`${base}.brief.${i}.selected`)} ${item.selected?'checked':''}><span><b>${E(item.kind.toUpperCase())}</b> · ${E(item.text)}</span></label>${sourceButton(p,item)}${item.date?`<p class="rubric">Confirmed date: ${E(dateLabel(item.date))}</p>`:''}</div>`).join('')}<p class="rubric">Next: select the relevant round and use Run script — Refresh preparation. Source-linked tasks will appear in this checklist and Reviews.</p></section>`;
}
function taskDocumentNote(p,t){
 const item=p.brief?.find(i=>i.id===t.requirementId);if(!item)return '';
 return `<div class="task-source">${sourceButton(p,item)}${!item.selected?pill('REQUIREMENT NO LONGER ACTIVE','orange'):''}<p>* ${E(p.company)} adaptation: connect your answer to “${E(item.text)}”. Use one verified CV example and explain its relevance; keep unsupported experience out.</p></div>`;
}
function printDocumentBrief(p){return !p.brief?.length?'':`<h2>Approved company requirements</h2>${p.brief.filter(i=>i.selected).map(i=>`<p><strong>${E(i.kind)}:</strong> ${E(i.text)}<br><small>${E(documentSource(p,i))}</small></p>`).join('')}`;}
function syncDocumentResult(result){state=result.state;version=result.version;dirty=false;status('All changes saved');render();notify(result.message);}
async function sendDocumentForm(url,form){
 const resp=await fetch(url,{method:'POST',headers:{'X-Workspace-Token':token},body:form});
 const result=await resp.json();if(!resp.ok)throw new Error(result.error||'Upload failed.');return result;
}
async function documentBlob(url,name){
 const resp=await fetch(url);if(!resp.ok){const r=await resp.json();throw new Error(r.error||'Download failed.');}
 const link=document.createElement('a'),urlObject=URL.createObjectURL(await resp.blob());link.href=urlObject;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(urlObject),1000);
}
document.addEventListener('click',async event=>{
 const el=event.target.closest('[data-action^="doc-"]');if(!el||busy)return;
 const action=el.dataset.action,p=currentProcess();
 try{
  if(action==='doc-source'){
   const d=p?.documents.find(d=>d.id===el.dataset.document);const pg=d?.pages.find(pg=>pg.number===Number(el.dataset.page));
   if(!pg)throw new Error('Source page not found.');
   modal(`<h2>${E(d.name)} · page ${pg.number}</h2><p class="muted">Current editable extraction. Check the original PDF if wording or layout is unclear.</p><pre>${E(pg.text)}</pre><a href="/api/documents/${encodeURIComponent(p.id)}/${encodeURIComponent(d.id)}/download" download>Download original PDF</a>`);return;
  }
  if(action==='doc-upload'){
   const files=Array.from($('#doc-files').files),kind=$('#doc-kind').value;
   if(!files.length)throw new Error('Choose at least one PDF.');
   if(files.some(f=>f.size>5*1024*1024||!f.name.toLowerCase().endsWith('.pdf')))throw new Error('Choose PDFs no larger than 5 MB each.');
   showBusy(true,'Reading your PDFs locally','No document text is sent to Gemini during upload.');
   try{
    await flush();let completed=0;
    for(const file of files){
     const form=new FormData();form.append('file',file);form.append('kind',kind);form.append('processId',p.id);form.append('version',version);
     try{const result=await sendDocumentForm('/api/documents/upload',form);state=result.state;version=result.version;completed++;}
     catch(e){render();throw new Error(`${completed} file(s) saved. ${file.name}: ${e.message}`);}
    }
    render();notify(`${completed} PDF(s) processed. Expand each file to review its extracted pages.`);
   }finally{showBusy(false);}return;
  }
  if(action==='doc-preview'){
   await flush();const r=await api('/api/documents/context',{method:'POST',body:JSON.stringify({processId:p.id,version})});
   modal('<h2>Document analysis: AI payload preview</h2><p class="muted">This text is sent only if you select Gemini and click Analyse documents. Remove confidential details from the editable page text before proceeding.</p><pre>'+E(JSON.stringify(r.context,null,2))+'</pre>');return;
  }
  if(action==='doc-analyse'||action==='doc-apply'){
   const mode=action==='doc-analyse'?$('#doc-mode').value:null;
   if(mode==='gemini'&&(!state.settings.aiConsent||!state.settings.freeTierConfirmed)){notify('Read and confirm the privacy/free-tier settings first.',true);location.hash='settings';return;}
   if(action==='doc-apply'&&!confirm('Apply the checked proposals? Selected company, role and deadline values will replace current values. Existing rounds, answers and completed tasks are preserved.'))return;
   showBusy(true,action==='doc-apply'?'Applying your selected details':'Analysing your documents',mode==='gemini'?'Sending the included text to Gemini for a reviewable draft.':'Using local text only. Existing preparation work is preserved.');
   try{await flush();const body={processId:p.id,version};if(mode)body.mode=mode;syncDocumentResult(await api(action==='doc-apply'?'/api/documents/apply':'/api/documents/analyse',{method:'POST',body:JSON.stringify(body)}));}finally{showBusy(false);}return;
  }
  if(action==='doc-archive'){
   await flush();await documentBlob('/api/documents/archive','sip-original-pdfs.zip');notify('Original PDF archive downloaded. Keep it with your JSON backup.');return;
  }
  if(action==='doc-restore-archive'){
   const f=$('#originals-file').files[0];if(!f)throw new Error('Choose the originals ZIP archive.');
   await flush();const form=new FormData();form.append('file',f);const result=await sendDocumentForm('/api/documents/archive',form);notify(result.message);return;
  }
 }catch(e){notify(e.message,true);}
});
