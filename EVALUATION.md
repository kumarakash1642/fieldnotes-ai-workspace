# Proposed evaluation — no results claimed

Create a labelled set of ten non-confidential or synthetic JDs/emails. Include contradictory dates, missing fields, long documents and irrelevant instructions embedded in document text. Hold some examples aside from prompt development.

Compare local extraction and Gemini on the same inputs:

| Measure | Definition |
|---|---|
| Fact precision | Correct extracted facts / all extracted facts |
| Fact recall | Correct required facts found / labelled required facts |
| Source support | Proposals correctly supported by the cited passage / all proposals |
| Critical errors | Incorrect deadline, company, role or unsupported mandatory requirement |
| Task usefulness | Human rating with a written reason and explicit requirement match |
| Performance | Response latency, failed runs and fallback frequency |
| Usage | Input/output tokens and estimated cost under the actual model/project pricing |

Record model ID, date, prompt version, sample size and failures. Schema validity is separate from factual accuracy. Do not substitute mocked API unit tests for live evaluation.

For a small user pilot, compare time and missed requirements on similar preparation tasks with 5–8 consenting participants. Counterbalance task order, remove personal information from published findings and describe the limited sample. Do not infer interview-selection effects.
