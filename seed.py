"""Public demonstration content. No personal CV or recruitment report is included."""
from copy import deepcopy
SECTIONS = [('personal', 'Personal story', 'A'),
 ('sales', 'Sales & CRM', 'A'),
 ('leadership', 'Student leadership', 'A'),
 ('marketing', 'Marketing', 'B'),
 ('operations', 'Operations & LSS', 'B'),
 ('analytics', 'Analytics & tools', 'B'),
 ('ai', 'AI & GenAI', 'B'),
 ('academics', 'Academics', 'C'),
 ('extras', 'Other CV items', 'C')]

QUESTIONS = [{'id': 'p1',
  'section': 'personal',
  'title': 'Tell me about yourself',
  'frames': {'Marketing · 30 seconds': '[FICTIONAL DEMO] I am Alex, a management student interested in improving '
                                       'everyday workflows. In a classroom project, I organised a task tracker to '
                                       'make responsibilities visible. I would use an internship to learn how '
                                       'teams translate customer needs into product decisions. Replace this '
                                       'fictional example with your own verified background.',
             'Marketing · 60 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                       'yourself: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this marketing · 60 seconds frame, distinguish '
                                       'your contribution from team results.',
             'Marketing · 90 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                       'yourself: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this marketing · 90 seconds frame, distinguish '
                                       'your contribution from team results.',
             'Operations · 30 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                        'yourself: state the context, your specific action, supporting evidence '
                                        'and what you learned. For this operations · 30 seconds frame, '
                                        'distinguish your contribution from team results.',
             'Operations · 60 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                        'yourself: state the context, your specific action, supporting evidence '
                                        'and what you learned. For this operations · 60 seconds frame, '
                                        'distinguish your contribution from team results.',
             'Operations · 90 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                        'yourself: state the context, your specific action, supporting evidence '
                                        'and what you learned. For this operations · 90 seconds frame, '
                                        'distinguish your contribution from team results.',
             'Analytics · 30 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                       'yourself: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this analytics · 30 seconds frame, distinguish '
                                       'your contribution from team results.',
             'Analytics · 60 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                       'yourself: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this analytics · 60 seconds frame, distinguish '
                                       'your contribution from team results.',
             'Analytics · 90 seconds': '[SAMPLE TEMPLATE — replace with your verified experience] Tell me about '
                                       'yourself: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this analytics · 90 seconds frame, distinguish '
                                       'your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'p2',
  'section': 'personal',
  'title': 'Walk me through your CV',
  'frames': {'60-second walkthrough': '[SAMPLE TEMPLATE — replace with your verified experience] Walk me through '
                                      'your CV: state the context, your specific action, supporting evidence and '
                                      'what you learned. For this 60-second walkthrough frame, distinguish your '
                                      'contribution from team results.',
             '90-second walkthrough': '[SAMPLE TEMPLATE — replace with your verified experience] Walk me through '
                                      'your CV: state the context, your specific action, supporting evidence and '
                                      'what you learned. For this 90-second walkthrough frame, distinguish your '
                                      'contribution from team results.',
             'Expected follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Walk me through '
                                    'your CV: state the context, your specific action, supporting evidence and '
                                    'what you learned. For this expected follow-ups frame, distinguish your '
                                    'contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'p3',
  'section': 'personal',
  'title': 'Why pursue an MBA?',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Why pursue an MBA?: state '
                             'the context, your specific action, supporting evidence and what you learned. For '
                             'this short answer frame, distinguish your contribution from team results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Why pursue an MBA?: '
                                'state the context, your specific action, supporting evidence and what you '
                                'learned. For this detailed answer frame, distinguish your contribution from team '
                                'results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Why pursue an '
                                         'MBA?: state the context, your specific action, supporting evidence and '
                                         'what you learned. For this evidence and calculation frame, distinguish '
                                         'your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Why pursue an MBA?: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this follow-up bank frame, distinguish your contribution from team '
                               'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'p4',
  'section': 'personal',
  'title': 'Why your institute?',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Why your institute?: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Why your '
                                       'institute?: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Why your institute?: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'p5',
  'section': 'personal',
  'title': 'Career goals and role fit',
  'frames': {'Marketing': '[SAMPLE TEMPLATE — replace with your verified experience] Career goals and role fit: '
                          'state the context, your specific action, supporting evidence and what you learned. For '
                          'this marketing frame, distinguish your contribution from team results.',
             'Operations': '[SAMPLE TEMPLATE — replace with your verified experience] Career goals and role fit: '
                           'state the context, your specific action, supporting evidence and what you learned. '
                           'For this operations frame, distinguish your contribution from team results.',
             'Analytics': '[SAMPLE TEMPLATE — replace with your verified experience] Career goals and role fit: '
                          'state the context, your specific action, supporting evidence and what you learned. For '
                          'this analytics frame, distinguish your contribution from team results.',
             'General management': '[SAMPLE TEMPLATE — replace with your verified experience] Career goals and '
                                   'role fit: state the context, your specific action, supporting evidence and '
                                   'what you learned. For this general management frame, distinguish your '
                                   'contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'p6',
  'section': 'personal',
  'title': 'Strength, weakness and feedback',
  'frames': {'Strength 1': '[SAMPLE TEMPLATE — replace with your verified experience] Strength, weakness and '
                           'feedback: state the context, your specific action, supporting evidence and what you '
                           'learned. For this strength 1 frame, distinguish your contribution from team results.',
             'Strength 2': '[SAMPLE TEMPLATE — replace with your verified experience] Strength, weakness and '
                           'feedback: state the context, your specific action, supporting evidence and what you '
                           'learned. For this strength 2 frame, distinguish your contribution from team results.',
             'Genuine weakness': '[SAMPLE TEMPLATE — replace with your verified experience] Strength, weakness '
                                 'and feedback: state the context, your specific action, supporting evidence and '
                                 'what you learned. For this genuine weakness frame, distinguish your '
                                 'contribution from team results.',
             'Recent feedback': '[SAMPLE TEMPLATE — replace with your verified experience] Strength, weakness and '
                                'feedback: state the context, your specific action, supporting evidence and what '
                                'you learned. For this recent feedback frame, distinguish your contribution from '
                                'team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 's1',
  'section': 'sales',
  'title': 'Explain revenue contribution',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Explain revenue '
                             'contribution: state the context, your specific action, supporting evidence and what '
                             'you learned. For this short answer frame, distinguish your contribution from team '
                             'results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Explain revenue '
                                'contribution: state the context, your specific action, supporting evidence and '
                                'what you learned. For this detailed answer frame, distinguish your contribution '
                                'from team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Explain '
                                         'revenue contribution: state the context, your specific action, '
                                         'supporting evidence and what you learned. For this evidence and '
                                         'calculation frame, distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Explain revenue '
                               'contribution: state the context, your specific action, supporting evidence and '
                               'what you learned. For this follow-up bank frame, distinguish your contribution '
                               'from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 's2',
  'section': 'sales',
  'title': 'Measure sales growth',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Measure sales growth: '
                             'state the context, your specific action, supporting evidence and what you learned. '
                             'For this short answer frame, distinguish your contribution from team results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Measure sales growth: '
                                'state the context, your specific action, supporting evidence and what you '
                                'learned. For this detailed answer frame, distinguish your contribution from team '
                                'results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Measure sales '
                                         'growth: state the context, your specific action, supporting evidence '
                                         'and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Measure sales growth: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this follow-up bank frame, distinguish your contribution from team '
                               'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 's3',
  'section': 'sales',
  'title': 'Measure repeat purchases',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Measure repeat purchases: '
                             'state the context, your specific action, supporting evidence and what you learned. '
                             'For this short answer frame, distinguish your contribution from team results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Measure repeat '
                                'purchases: state the context, your specific action, supporting evidence and what '
                                'you learned. For this detailed answer frame, distinguish your contribution from '
                                'team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Measure '
                                         'repeat purchases: state the context, your specific action, supporting '
                                         'evidence and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Measure repeat '
                               'purchases: state the context, your specific action, supporting evidence and what '
                               'you learned. For this follow-up bank frame, distinguish your contribution from '
                               'team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 's4',
  'section': 'sales',
  'title': 'Consultative selling story',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Consultative selling '
                             'story: state the context, your specific action, supporting evidence and what you '
                             'learned. For this short answer frame, distinguish your contribution from team '
                             'results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Consultative selling '
                                'story: state the context, your specific action, supporting evidence and what you '
                                'learned. For this detailed answer frame, distinguish your contribution from team '
                                'results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Consultative '
                                         'selling story: state the context, your specific action, supporting '
                                         'evidence and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Consultative selling '
                               'story: state the context, your specific action, supporting evidence and what you '
                               'learned. For this follow-up bank frame, distinguish your contribution from team '
                               'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 's5',
  'section': 'sales',
  'title': 'Sales metrics and formulas',
  'frames': {'Concept': '[SAMPLE TEMPLATE — replace with your verified experience] Sales metrics and formulas: '
                        'state the context, your specific action, supporting evidence and what you learned. For '
                        'this concept frame, distinguish your contribution from team results.',
             'Formula and example': '[SAMPLE TEMPLATE — replace with your verified experience] Sales metrics and '
                                    'formulas: state the context, your specific action, supporting evidence and '
                                    'what you learned. For this formula and example frame, distinguish your '
                                    'contribution from team results.',
             'Application': '[SAMPLE TEMPLATE — replace with your verified experience] Sales metrics and '
                            'formulas: state the context, your specific action, supporting evidence and what you '
                            'learned. For this application frame, distinguish your contribution from team '
                            'results.',
             'Limitations': '[SAMPLE TEMPLATE — replace with your verified experience] Sales metrics and '
                            'formulas: state the context, your specific action, supporting evidence and what you '
                            'learned. For this limitations frame, distinguish your contribution from team '
                            'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 's6',
  'section': 'sales',
  'title': 'Difficult customer and failed sale',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Difficult customer and '
                             'failed sale: state the context, your specific action, supporting evidence and what '
                             'you learned. For this short answer frame, distinguish your contribution from team '
                             'results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Difficult customer and '
                                'failed sale: state the context, your specific action, supporting evidence and '
                                'what you learned. For this detailed answer frame, distinguish your contribution '
                                'from team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Difficult '
                                         'customer and failed sale: state the context, your specific action, '
                                         'supporting evidence and what you learned. For this evidence and '
                                         'calculation frame, distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Difficult customer and '
                               'failed sale: state the context, your specific action, supporting evidence and '
                               'what you learned. For this follow-up bank frame, distinguish your contribution '
                               'from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'o1',
  'section': 'leadership',
  'title': 'Evaluate campaign reach',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Evaluate campaign reach: '
                             'state the context, your specific action, supporting evidence and what you learned. '
                             'For this short answer frame, distinguish your contribution from team results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Evaluate campaign '
                                'reach: state the context, your specific action, supporting evidence and what you '
                                'learned. For this detailed answer frame, distinguish your contribution from team '
                                'results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Evaluate '
                                         'campaign reach: state the context, your specific action, supporting '
                                         'evidence and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Evaluate campaign '
                               'reach: state the context, your specific action, supporting evidence and what you '
                               'learned. For this follow-up bank frame, distinguish your contribution from team '
                               'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'o2',
  'section': 'leadership',
  'title': 'Explain budget management',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Explain budget '
                             'management: state the context, your specific action, supporting evidence and what '
                             'you learned. For this short answer frame, distinguish your contribution from team '
                             'results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Explain budget '
                                'management: state the context, your specific action, supporting evidence and '
                                'what you learned. For this detailed answer frame, distinguish your contribution '
                                'from team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Explain '
                                         'budget management: state the context, your specific action, supporting '
                                         'evidence and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Explain budget '
                               'management: state the context, your specific action, supporting evidence and what '
                               'you learned. For this follow-up bank frame, distinguish your contribution from '
                               'team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'o3',
  'section': 'leadership',
  'title': 'Negotiation example',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Negotiation example: '
                             'state the context, your specific action, supporting evidence and what you learned. '
                             'For this short answer frame, distinguish your contribution from team results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Negotiation example: '
                                'state the context, your specific action, supporting evidence and what you '
                                'learned. For this detailed answer frame, distinguish your contribution from team '
                                'results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Negotiation '
                                         'example: state the context, your specific action, supporting evidence '
                                         'and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Negotiation example: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this follow-up bank frame, distinguish your contribution from team '
                               'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'o4',
  'section': 'leadership',
  'title': 'Event execution example',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Event execution example: '
                             'state the context, your specific action, supporting evidence and what you learned. '
                             'For this short answer frame, distinguish your contribution from team results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Event execution '
                                'example: state the context, your specific action, supporting evidence and what '
                                'you learned. For this detailed answer frame, distinguish your contribution from '
                                'team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Event '
                                         'execution example: state the context, your specific action, supporting '
                                         'evidence and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Event execution '
                               'example: state the context, your specific action, supporting evidence and what '
                               'you learned. For this follow-up bank frame, distinguish your contribution from '
                               'team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'o5',
  'section': 'leadership',
  'title': 'Audience growth calculations',
  'frames': {'Concept': '[SAMPLE TEMPLATE — replace with your verified experience] Audience growth calculations: '
                        'state the context, your specific action, supporting evidence and what you learned. For '
                        'this concept frame, distinguish your contribution from team results.',
             'Formula and example': '[SAMPLE TEMPLATE — replace with your verified experience] Audience growth '
                                    'calculations: state the context, your specific action, supporting evidence '
                                    'and what you learned. For this formula and example frame, distinguish your '
                                    'contribution from team results.',
             'Application': '[SAMPLE TEMPLATE — replace with your verified experience] Audience growth '
                            'calculations: state the context, your specific action, supporting evidence and what '
                            'you learned. For this application frame, distinguish your contribution from team '
                            'results.',
             'Limitations': '[SAMPLE TEMPLATE — replace with your verified experience] Audience growth '
                            'calculations: state the context, your specific action, supporting evidence and what '
                            'you learned. For this limitations frame, distinguish your contribution from team '
                            'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'o6',
  'section': 'leadership',
  'title': 'Content initiative',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Content initiative: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Content '
                                       'initiative: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Content initiative: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'm1',
  'section': 'marketing',
  'title': 'Marketing simulation defence',
  'frames': {'60-second summary': '[SAMPLE TEMPLATE — replace with your verified experience] Marketing simulation '
                                  'defence: state the context, your specific action, supporting evidence and what '
                                  'you learned. For this 60-second summary frame, distinguish your contribution '
                                  'from team results.',
             'Detailed defence': '[SAMPLE TEMPLATE — replace with your verified experience] Marketing simulation '
                                 'defence: state the context, your specific action, supporting evidence and what '
                                 'you learned. For this detailed defence frame, distinguish your contribution '
                                 'from team results.',
             'My exact contribution': '[SAMPLE TEMPLATE — replace with your verified experience] Marketing '
                                      'simulation defence: state the context, your specific action, supporting '
                                      'evidence and what you learned. For this my exact contribution frame, '
                                      'distinguish your contribution from team results.',
             'Likely follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Marketing simulation '
                                  'defence: state the context, your specific action, supporting evidence and what '
                                  'you learned. For this likely follow-ups frame, distinguish your contribution '
                                  'from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'm2',
  'section': 'marketing',
  'title': 'STP and positioning',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] STP and positioning: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] STP and '
                                       'positioning: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] STP and positioning: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'm3',
  'section': 'marketing',
  'title': 'Customer journey and funnel',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Customer journey and '
                               'funnel: state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Customer '
                                       'journey and funnel: state the context, your specific action, supporting '
                                       'evidence and what you learned. For this example or application frame, '
                                       'distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Customer journey and '
                           'funnel: state the context, your specific action, supporting evidence and what you '
                           'learned. For this follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'm4',
  'section': 'marketing',
  'title': 'Omnichannel vs multichannel',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Omnichannel vs '
                               'multichannel: state the context, your specific action, supporting evidence and '
                               'what you learned. For this primary answer frame, distinguish your contribution '
                               'from team results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Omnichannel vs '
                                       'multichannel: state the context, your specific action, supporting '
                                       'evidence and what you learned. For this example or application frame, '
                                       'distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Omnichannel vs '
                           'multichannel: state the context, your specific action, supporting evidence and what '
                           'you learned. For this follow-ups frame, distinguish your contribution from team '
                           'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'm5',
  'section': 'marketing',
  'title': 'Digital campaign metrics',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Digital campaign '
                               'metrics: state the context, your specific action, supporting evidence and what '
                               'you learned. For this primary answer frame, distinguish your contribution from '
                               'team results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Digital '
                                       'campaign metrics: state the context, your specific action, supporting '
                                       'evidence and what you learned. For this example or application frame, '
                                       'distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Digital campaign metrics: '
                           'state the context, your specific action, supporting evidence and what you learned. '
                           'For this follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'l1',
  'section': 'operations',
  'title': 'DMAIC application',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] DMAIC application: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] DMAIC '
                                       'application: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] DMAIC application: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'l2',
  'section': 'operations',
  'title': 'SIPOC, VOC and CTQ',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] SIPOC, VOC and CTQ: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] SIPOC, VOC and '
                                       'CTQ: state the context, your specific action, supporting evidence and '
                                       'what you learned. For this example or application frame, distinguish your '
                                       'contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] SIPOC, VOC and CTQ: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'l3',
  'section': 'operations',
  'title': 'Root-cause toolkit',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Root-cause toolkit: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Root-cause '
                                       'toolkit: state the context, your specific action, supporting evidence and '
                                       'what you learned. For this example or application frame, distinguish your '
                                       'contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Root-cause toolkit: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'l4',
  'section': 'operations',
  'title': 'Cp, Cpk and DPMO',
  'frames': {'Concept': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk and DPMO: state the '
                        'context, your specific action, supporting evidence and what you learned. For this '
                        'concept frame, distinguish your contribution from team results.',
             'Formula and example': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk and DPMO: '
                                    'state the context, your specific action, supporting evidence and what you '
                                    'learned. For this formula and example frame, distinguish your contribution '
                                    'from team results.',
             'Application': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk and DPMO: state '
                            'the context, your specific action, supporting evidence and what you learned. For '
                            'this application frame, distinguish your contribution from team results.',
             'Limitations': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk and DPMO: state '
                            'the context, your specific action, supporting evidence and what you learned. For '
                            'this limitations frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'l5',
  'section': 'operations',
  'title': 'FMEA and control plan',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] FMEA and control plan: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] FMEA and '
                                       'control plan: state the context, your specific action, supporting '
                                       'evidence and what you learned. For this example or application frame, '
                                       'distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] FMEA and control plan: '
                           'state the context, your specific action, supporting evidence and what you learned. '
                           'For this follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'a1',
  'section': 'analytics',
  'title': 'Excel practical readiness',
  'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified experience] Excel practical '
                                      'readiness: state the context, your specific action, supporting evidence '
                                      'and what you learned. For this interview explanation frame, distinguish '
                                      'your contribution from team results.',
             'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified experience] Excel '
                                          'practical readiness: state the context, your specific action, '
                                          'supporting evidence and what you learned. For this practical example '
                                          'or code frame, distinguish your contribution from team results.',
             'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] Excel practical '
                                 'readiness: state the context, your specific action, supporting evidence and '
                                 'what you learned. For this project evidence frame, distinguish your '
                                 'contribution from team results.',
             'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Excel practical '
                                     'readiness: state the context, your specific action, supporting evidence and '
                                     'what you learned. For this technical follow-ups frame, distinguish your '
                                     'contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'a2',
  'section': 'analytics',
  'title': 'SQL core queries',
  'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified experience] SQL core '
                                      'queries: state the context, your specific action, supporting evidence and '
                                      'what you learned. For this interview explanation frame, distinguish your '
                                      'contribution from team results.',
             'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified experience] SQL core '
                                          'queries: state the context, your specific action, supporting evidence '
                                          'and what you learned. For this practical example or code frame, '
                                          'distinguish your contribution from team results.',
             'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] SQL core queries: '
                                 'state the context, your specific action, supporting evidence and what you '
                                 'learned. For this project evidence frame, distinguish your contribution from '
                                 'team results.',
             'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] SQL core queries: '
                                     'state the context, your specific action, supporting evidence and what you '
                                     'learned. For this technical follow-ups frame, distinguish your contribution '
                                     'from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'a3',
  'section': 'analytics',
  'title': 'SQL intermediate concepts',
  'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified experience] SQL intermediate '
                                      'concepts: state the context, your specific action, supporting evidence and '
                                      'what you learned. For this interview explanation frame, distinguish your '
                                      'contribution from team results.',
             'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified experience] SQL '
                                          'intermediate concepts: state the context, your specific action, '
                                          'supporting evidence and what you learned. For this practical example '
                                          'or code frame, distinguish your contribution from team results.',
             'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] SQL intermediate '
                                 'concepts: state the context, your specific action, supporting evidence and what '
                                 'you learned. For this project evidence frame, distinguish your contribution '
                                 'from team results.',
             'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] SQL intermediate '
                                     'concepts: state the context, your specific action, supporting evidence and '
                                     'what you learned. For this technical follow-ups frame, distinguish your '
                                     'contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'a4',
  'section': 'analytics',
  'title': 'Power BI dashboard defence',
  'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified experience] Power BI '
                                      'dashboard defence: state the context, your specific action, supporting '
                                      'evidence and what you learned. For this interview explanation frame, '
                                      'distinguish your contribution from team results.',
             'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified experience] Power BI '
                                          'dashboard defence: state the context, your specific action, supporting '
                                          'evidence and what you learned. For this practical example or code '
                                          'frame, distinguish your contribution from team results.',
             'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] Power BI dashboard '
                                 'defence: state the context, your specific action, supporting evidence and what '
                                 'you learned. For this project evidence frame, distinguish your contribution '
                                 'from team results.',
             'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Power BI '
                                     'dashboard defence: state the context, your specific action, supporting '
                                     'evidence and what you learned. For this technical follow-ups frame, '
                                     'distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'a5',
  'section': 'analytics',
  'title': 'One flagship analytics project',
  'frames': {'60-second summary': '[SAMPLE TEMPLATE — replace with your verified experience] One flagship '
                                  'analytics project: state the context, your specific action, supporting '
                                  'evidence and what you learned. For this 60-second summary frame, distinguish '
                                  'your contribution from team results.',
             'Detailed defence': '[SAMPLE TEMPLATE — replace with your verified experience] One flagship '
                                 'analytics project: state the context, your specific action, supporting evidence '
                                 'and what you learned. For this detailed defence frame, distinguish your '
                                 'contribution from team results.',
             'My exact contribution': '[SAMPLE TEMPLATE — replace with your verified experience] One flagship '
                                      'analytics project: state the context, your specific action, supporting '
                                      'evidence and what you learned. For this my exact contribution frame, '
                                      'distinguish your contribution from team results.',
             'Likely follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] One flagship '
                                  'analytics project: state the context, your specific action, supporting '
                                  'evidence and what you learned. For this likely follow-ups frame, distinguish '
                                  'your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ai1',
  'section': 'ai',
  'title': 'Clarify your proficiency level',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Clarify your proficiency '
                             'level: state the context, your specific action, supporting evidence and what you '
                             'learned. For this short answer frame, distinguish your contribution from team '
                             'results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Clarify your '
                                'proficiency level: state the context, your specific action, supporting evidence '
                                'and what you learned. For this detailed answer frame, distinguish your '
                                'contribution from team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Clarify your '
                                         'proficiency level: state the context, your specific action, supporting '
                                         'evidence and what you learned. For this evidence and calculation frame, '
                                         'distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Clarify your '
                               'proficiency level: state the context, your specific action, supporting evidence '
                               'and what you learned. For this follow-up bank frame, distinguish your '
                               'contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ai2',
  'section': 'ai',
  'title': 'AI, ML and GenAI distinctions',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] AI, ML and GenAI '
                               'distinctions: state the context, your specific action, supporting evidence and '
                               'what you learned. For this primary answer frame, distinguish your contribution '
                               'from team results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] AI, ML and '
                                       'GenAI distinctions: state the context, your specific action, supporting '
                                       'evidence and what you learned. For this example or application frame, '
                                       'distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] AI, ML and GenAI '
                           'distinctions: state the context, your specific action, supporting evidence and what '
                           'you learned. For this follow-ups frame, distinguish your contribution from team '
                           'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ai3',
  'section': 'ai',
  'title': 'ML workflow and evaluation',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] ML workflow and '
                               'evaluation: state the context, your specific action, supporting evidence and what '
                               'you learned. For this primary answer frame, distinguish your contribution from '
                               'team results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] ML workflow and '
                                       'evaluation: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] ML workflow and evaluation: '
                           'state the context, your specific action, supporting evidence and what you learned. '
                           'For this follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ai4',
  'section': 'ai',
  'title': 'Personal AI project defence',
  'frames': {'60-second summary': '[SAMPLE TEMPLATE — replace with your verified experience] Personal AI project '
                                  'defence: state the context, your specific action, supporting evidence and what '
                                  'you learned. For this 60-second summary frame, distinguish your contribution '
                                  'from team results.',
             'Detailed defence': '[SAMPLE TEMPLATE — replace with your verified experience] Personal AI project '
                                 'defence: state the context, your specific action, supporting evidence and what '
                                 'you learned. For this detailed defence frame, distinguish your contribution '
                                 'from team results.',
             'My exact contribution': '[SAMPLE TEMPLATE — replace with your verified experience] Personal AI '
                                      'project defence: state the context, your specific action, supporting '
                                      'evidence and what you learned. For this my exact contribution frame, '
                                      'distinguish your contribution from team results.',
             'Likely follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Personal AI project '
                                  'defence: state the context, your specific action, supporting evidence and what '
                                  'you learned. For this likely follow-ups frame, distinguish your contribution '
                                  'from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ac1',
  'section': 'academics',
  'title': 'Academic strengths',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Academic strengths: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Academic '
                                       'strengths: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Academic strengths: state '
                           'the context, your specific action, supporting evidence and what you learned. For this '
                           'follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ac2',
  'section': 'academics',
  'title': 'Academic learning in business',
  'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Academic learning in '
                             'business: state the context, your specific action, supporting evidence and what you '
                             'learned. For this short answer frame, distinguish your contribution from team '
                             'results.',
             'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Academic learning in '
                                'business: state the context, your specific action, supporting evidence and what '
                                'you learned. For this detailed answer frame, distinguish your contribution from '
                                'team results.',
             'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified experience] Academic '
                                         'learning in business: state the context, your specific action, '
                                         'supporting evidence and what you learned. For this evidence and '
                                         'calculation frame, distinguish your contribution from team results.',
             'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Academic learning in '
                               'business: state the context, your specific action, supporting evidence and what '
                               'you learned. For this follow-up bank frame, distinguish your contribution from '
                               'team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ac3',
  'section': 'academics',
  'title': 'Academic performance explanation',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Academic performance '
                               'explanation: state the context, your specific action, supporting evidence and '
                               'what you learned. For this primary answer frame, distinguish your contribution '
                               'from team results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Academic '
                                       'performance explanation: state the context, your specific action, '
                                       'supporting evidence and what you learned. For this example or application '
                                       'frame, distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Academic performance '
                           'explanation: state the context, your specific action, supporting evidence and what '
                           'you learned. For this follow-ups frame, distinguish your contribution from team '
                           'results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'ac4',
  'section': 'academics',
  'title': 'Learning and improvement',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Learning and '
                               'improvement: state the context, your specific action, supporting evidence and '
                               'what you learned. For this primary answer frame, distinguish your contribution '
                               'from team results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Learning and '
                                       'improvement: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this example or application frame, distinguish '
                                       'your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Learning and improvement: '
                           'state the context, your specific action, supporting evidence and what you learned. '
                           'For this follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'e1',
  'section': 'extras',
  'title': 'Creative collaboration',
  'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Creative collaboration: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this primary answer frame, distinguish your contribution from team '
                               'results.',
             'Example or application': '[SAMPLE TEMPLATE — replace with your verified experience] Creative '
                                       'collaboration: state the context, your specific action, supporting '
                                       'evidence and what you learned. For this example or application frame, '
                                       'distinguish your contribution from team results.',
             'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Creative collaboration: '
                           'state the context, your specific action, supporting evidence and what you learned. '
                           'For this follow-ups frame, distinguish your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'e2',
  'section': 'extras',
  'title': 'Course learning',
  'frames': {'Concise answer': '[SAMPLE TEMPLATE — replace with your verified experience] Course learning: state '
                               'the context, your specific action, supporting evidence and what you learned. For '
                               'this concise answer frame, distinguish your contribution from team results.',
             'Learning and relevance': '[SAMPLE TEMPLATE — replace with your verified experience] Course '
                                       'learning: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this learning and relevance frame, distinguish '
                                       'your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']},
 {'id': 'e3',
  'section': 'extras',
  'title': 'Conference learning',
  'frames': {'Concise answer': '[SAMPLE TEMPLATE — replace with your verified experience] Conference learning: '
                               'state the context, your specific action, supporting evidence and what you '
                               'learned. For this concise answer frame, distinguish your contribution from team '
                               'results.',
             'Learning and relevance': '[SAMPLE TEMPLATE — replace with your verified experience] Conference '
                                       'learning: state the context, your specific action, supporting evidence '
                                       'and what you learned. For this learning and relevance frame, distinguish '
                                       'your contribution from team results.'},
  'improve': 'Add a concrete decision, explain alternatives and use verified results only.',
  'evidence': 'An original artefact, a clear calculation and a precise account of personal contribution.',
  'follow': 'What did you personally do? What failed? How did you measure the result?',
  'adaptations': ['Sales role: connect a verified example to customer needs in the actual JD.',
                  'Product role: explain the problem, trade-off and how you would measure success.']}]

COMPANIES = [{'name': 'Example Retail',
  'sector': 'Retail',
  'source': 'Fictional demo',
  'note': 'Fictional company for demonstration; no recruitment claim.'},
 {'name': 'Example Software',
  'sector': 'Technology',
  'source': 'Fictional demo',
  'note': 'Fictional company for demonstration; no recruitment claim.'}]

EVIDENCE = [('project',
  'Project contribution',
  'ai4',
  'Identify the artefact, your decisions and implementation assistance.'),
 ('metric', 'Measured outcome', 's2', 'Verify the baseline, denominator, dates and attribution.')]

_INITIAL = {'answers': {'p1': {'frames': {'Marketing · 30 seconds': '[FICTIONAL DEMO] I am Alex, a management student '
                                                         'interested in improving everyday workflows. In a '
                                                         'classroom project, I organised a task tracker to make '
                                                         'responsibilities visible. I would use an internship to '
                                                         'learn how teams translate customer needs into product '
                                                         'decisions. Replace this fictional example with your own '
                                                         'verified background.',
                               'Marketing · 60 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Tell me about yourself: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this marketing · 60 seconds frame, '
                                                         'distinguish your contribution from team results.',
                               'Marketing · 90 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Tell me about yourself: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this marketing · 90 seconds frame, '
                                                         'distinguish your contribution from team results.',
                               'Operations · 30 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] Tell me about yourself: state the context, '
                                                          'your specific action, supporting evidence and what you '
                                                          'learned. For this operations · 30 seconds frame, '
                                                          'distinguish your contribution from team results.',
                               'Operations · 60 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] Tell me about yourself: state the context, '
                                                          'your specific action, supporting evidence and what you '
                                                          'learned. For this operations · 60 seconds frame, '
                                                          'distinguish your contribution from team results.',
                               'Operations · 90 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] Tell me about yourself: state the context, '
                                                          'your specific action, supporting evidence and what you '
                                                          'learned. For this operations · 90 seconds frame, '
                                                          'distinguish your contribution from team results.',
                               'Analytics · 30 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Tell me about yourself: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this analytics · 30 seconds frame, '
                                                         'distinguish your contribution from team results.',
                               'Analytics · 60 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Tell me about yourself: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this analytics · 60 seconds frame, '
                                                         'distinguish your contribution from team results.',
                               'Analytics · 90 seconds': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Tell me about yourself: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this analytics · 90 seconds frame, '
                                                         'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'p2': {'frames': {'60-second walkthrough': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] Walk me through your CV: state the context, '
                                                        'your specific action, supporting evidence and what you '
                                                        'learned. For this 60-second walkthrough frame, '
                                                        'distinguish your contribution from team results.',
                               '90-second walkthrough': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] Walk me through your CV: state the context, '
                                                        'your specific action, supporting evidence and what you '
                                                        'learned. For this 90-second walkthrough frame, '
                                                        'distinguish your contribution from team results.',
                               'Expected follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                      'Walk me through your CV: state the context, your specific '
                                                      'action, supporting evidence and what you learned. For this '
                                                      'expected follow-ups frame, distinguish your contribution '
                                                      'from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'p3': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Why '
                                               'pursue an MBA?: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] Why '
                                                  'pursue an MBA?: state the context, your specific action, '
                                                  'supporting evidence and what you learned. For this detailed '
                                                  'answer frame, distinguish your contribution from team results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Why pursue an MBA?: state the context, '
                                                           'your specific action, supporting evidence and what '
                                                           'you learned. For this evidence and calculation frame, '
                                                           'distinguish your contribution from team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Why '
                                                 'pursue an MBA?: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this follow-up '
                                                 'bank frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'p4': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] Why '
                                                 'your institute?: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Why your institute?: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Why your '
                                             'institute?: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'p5': {'frames': {'Marketing': '[SAMPLE TEMPLATE — replace with your verified experience] Career '
                                            'goals and role fit: state the context, your specific action, '
                                            'supporting evidence and what you learned. For this marketing frame, '
                                            'distinguish your contribution from team results.',
                               'Operations': '[SAMPLE TEMPLATE — replace with your verified experience] Career '
                                             'goals and role fit: state the context, your specific action, '
                                             'supporting evidence and what you learned. For this operations '
                                             'frame, distinguish your contribution from team results.',
                               'Analytics': '[SAMPLE TEMPLATE — replace with your verified experience] Career '
                                            'goals and role fit: state the context, your specific action, '
                                            'supporting evidence and what you learned. For this analytics frame, '
                                            'distinguish your contribution from team results.',
                               'General management': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                     'Career goals and role fit: state the context, your specific '
                                                     'action, supporting evidence and what you learned. For this '
                                                     'general management frame, distinguish your contribution '
                                                     'from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'p6': {'frames': {'Strength 1': '[SAMPLE TEMPLATE — replace with your verified experience] Strength, '
                                             'weakness and feedback: state the context, your specific action, '
                                             'supporting evidence and what you learned. For this strength 1 '
                                             'frame, distinguish your contribution from team results.',
                               'Strength 2': '[SAMPLE TEMPLATE — replace with your verified experience] Strength, '
                                             'weakness and feedback: state the context, your specific action, '
                                             'supporting evidence and what you learned. For this strength 2 '
                                             'frame, distinguish your contribution from team results.',
                               'Genuine weakness': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                   'Strength, weakness and feedback: state the context, your '
                                                   'specific action, supporting evidence and what you learned. '
                                                   'For this genuine weakness frame, distinguish your '
                                                   'contribution from team results.',
                               'Recent feedback': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Strength, weakness and feedback: state the context, your '
                                                  'specific action, supporting evidence and what you learned. For '
                                                  'this recent feedback frame, distinguish your contribution from '
                                                  'team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             's1': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Explain '
                                               'revenue contribution: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Explain revenue contribution: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'detailed answer frame, distinguish your contribution from team '
                                                  'results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Explain revenue contribution: state the '
                                                           'context, your specific action, supporting evidence '
                                                           'and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Explain revenue contribution: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'follow-up bank frame, distinguish your contribution from team '
                                                 'results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             's2': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Measure '
                                               'sales growth: state the context, your specific action, supporting '
                                               'evidence and what you learned. For this short answer frame, '
                                               'distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Measure sales growth: state the context, your specific action, '
                                                  'supporting evidence and what you learned. For this detailed '
                                                  'answer frame, distinguish your contribution from team results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Measure sales growth: state the context, '
                                                           'your specific action, supporting evidence and what '
                                                           'you learned. For this evidence and calculation frame, '
                                                           'distinguish your contribution from team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Measure sales growth: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this follow-up '
                                                 'bank frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             's3': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Measure '
                                               'repeat purchases: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Measure repeat purchases: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'detailed answer frame, distinguish your contribution from team '
                                                  'results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Measure repeat purchases: state the '
                                                           'context, your specific action, supporting evidence '
                                                           'and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Measure repeat purchases: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'follow-up bank frame, distinguish your contribution from team '
                                                 'results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             's4': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                               'Consultative selling story: state the context, your specific '
                                               'action, supporting evidence and what you learned. For this short '
                                               'answer frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Consultative selling story: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'detailed answer frame, distinguish your contribution from team '
                                                  'results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Consultative selling story: state the '
                                                           'context, your specific action, supporting evidence '
                                                           'and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Consultative selling story: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'follow-up bank frame, distinguish your contribution from team '
                                                 'results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             's5': {'frames': {'Concept': '[SAMPLE TEMPLATE — replace with your verified experience] Sales '
                                          'metrics and formulas: state the context, your specific action, '
                                          'supporting evidence and what you learned. For this concept frame, '
                                          'distinguish your contribution from team results.',
                               'Formula and example': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                      'Sales metrics and formulas: state the context, your '
                                                      'specific action, supporting evidence and what you learned. '
                                                      'For this formula and example frame, distinguish your '
                                                      'contribution from team results.',
                               'Application': '[SAMPLE TEMPLATE — replace with your verified experience] Sales '
                                              'metrics and formulas: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this application '
                                              'frame, distinguish your contribution from team results.',
                               'Limitations': '[SAMPLE TEMPLATE — replace with your verified experience] Sales '
                                              'metrics and formulas: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this limitations '
                                              'frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             's6': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                               'Difficult customer and failed sale: state the context, your '
                                               'specific action, supporting evidence and what you learned. For '
                                               'this short answer frame, distinguish your contribution from team '
                                               'results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Difficult customer and failed sale: state the context, your '
                                                  'specific action, supporting evidence and what you learned. For '
                                                  'this detailed answer frame, distinguish your contribution from '
                                                  'team results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Difficult customer and failed sale: state '
                                                           'the context, your specific action, supporting '
                                                           'evidence and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Difficult customer and failed sale: state the context, your '
                                                 'specific action, supporting evidence and what you learned. For '
                                                 'this follow-up bank frame, distinguish your contribution from '
                                                 'team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'o1': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                               'Evaluate campaign reach: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Evaluate campaign reach: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'detailed answer frame, distinguish your contribution from team '
                                                  'results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Evaluate campaign reach: state the '
                                                           'context, your specific action, supporting evidence '
                                                           'and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Evaluate campaign reach: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'follow-up bank frame, distinguish your contribution from team '
                                                 'results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'o2': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Explain '
                                               'budget management: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Explain budget management: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'detailed answer frame, distinguish your contribution from team '
                                                  'results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Explain budget management: state the '
                                                           'context, your specific action, supporting evidence '
                                                           'and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Explain budget management: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'follow-up bank frame, distinguish your contribution from team '
                                                 'results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'o3': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                               'Negotiation example: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Negotiation example: state the context, your specific action, '
                                                  'supporting evidence and what you learned. For this detailed '
                                                  'answer frame, distinguish your contribution from team results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Negotiation example: state the context, '
                                                           'your specific action, supporting evidence and what '
                                                           'you learned. For this evidence and calculation frame, '
                                                           'distinguish your contribution from team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Negotiation example: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this follow-up '
                                                 'bank frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'o4': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] Event '
                                               'execution example: state the context, your specific action, '
                                               'supporting evidence and what you learned. For this short answer '
                                               'frame, distinguish your contribution from team results.',
                               'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Event execution example: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'detailed answer frame, distinguish your contribution from team '
                                                  'results.',
                               'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                           'experience] Event execution example: state the '
                                                           'context, your specific action, supporting evidence '
                                                           'and what you learned. For this evidence and '
                                                           'calculation frame, distinguish your contribution from '
                                                           'team results.',
                               'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] Event '
                                                 'execution example: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this follow-up '
                                                 'bank frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'o5': {'frames': {'Concept': '[SAMPLE TEMPLATE — replace with your verified experience] Audience '
                                          'growth calculations: state the context, your specific action, '
                                          'supporting evidence and what you learned. For this concept frame, '
                                          'distinguish your contribution from team results.',
                               'Formula and example': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                      'Audience growth calculations: state the context, your '
                                                      'specific action, supporting evidence and what you learned. '
                                                      'For this formula and example frame, distinguish your '
                                                      'contribution from team results.',
                               'Application': '[SAMPLE TEMPLATE — replace with your verified experience] Audience '
                                              'growth calculations: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this application '
                                              'frame, distinguish your contribution from team results.',
                               'Limitations': '[SAMPLE TEMPLATE — replace with your verified experience] Audience '
                                              'growth calculations: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this limitations '
                                              'frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'o6': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Content initiative: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Content initiative: state the context, your '
                                                         'specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Content '
                                             'initiative: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'm1': {'frames': {'60-second summary': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                    'Marketing simulation defence: state the context, your '
                                                    'specific action, supporting evidence and what you learned. '
                                                    'For this 60-second summary frame, distinguish your '
                                                    'contribution from team results.',
                               'Detailed defence': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                   'Marketing simulation defence: state the context, your '
                                                   'specific action, supporting evidence and what you learned. '
                                                   'For this detailed defence frame, distinguish your '
                                                   'contribution from team results.',
                               'My exact contribution': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] Marketing simulation defence: state the '
                                                        'context, your specific action, supporting evidence and '
                                                        'what you learned. For this my exact contribution frame, '
                                                        'distinguish your contribution from team results.',
                               'Likely follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                    'Marketing simulation defence: state the context, your '
                                                    'specific action, supporting evidence and what you learned. '
                                                    'For this likely follow-ups frame, distinguish your '
                                                    'contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'm2': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] STP '
                                                 'and positioning: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] STP and positioning: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] STP and '
                                             'positioning: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'm3': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Customer journey and funnel: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'primary answer frame, distinguish your contribution from team '
                                                 'results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Customer journey and funnel: state the '
                                                         'context, your specific action, supporting evidence and '
                                                         'what you learned. For this example or application '
                                                         'frame, distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Customer '
                                             'journey and funnel: state the context, your specific action, '
                                             'supporting evidence and what you learned. For this follow-ups '
                                             'frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'm4': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Omnichannel vs multichannel: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'primary answer frame, distinguish your contribution from team '
                                                 'results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Omnichannel vs multichannel: state the '
                                                         'context, your specific action, supporting evidence and '
                                                         'what you learned. For this example or application '
                                                         'frame, distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                             'Omnichannel vs multichannel: state the context, your specific '
                                             'action, supporting evidence and what you learned. For this '
                                             'follow-ups frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'm5': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Digital campaign metrics: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'primary answer frame, distinguish your contribution from team '
                                                 'results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Digital campaign metrics: state the '
                                                         'context, your specific action, supporting evidence and '
                                                         'what you learned. For this example or application '
                                                         'frame, distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Digital '
                                             'campaign metrics: state the context, your specific action, '
                                             'supporting evidence and what you learned. For this follow-ups '
                                             'frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'l1': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] DMAIC '
                                                 'application: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] DMAIC application: state the context, your '
                                                         'specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] DMAIC '
                                             'application: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'l2': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'SIPOC, VOC and CTQ: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] SIPOC, VOC and CTQ: state the context, your '
                                                         'specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] SIPOC, '
                                             'VOC and CTQ: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'l3': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Root-cause toolkit: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Root-cause toolkit: state the context, your '
                                                         'specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                             'Root-cause toolkit: state the context, your specific action, '
                                             'supporting evidence and what you learned. For this follow-ups '
                                             'frame, distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'l4': {'frames': {'Concept': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk and '
                                          'DPMO: state the context, your specific action, supporting evidence and '
                                          'what you learned. For this concept frame, distinguish your '
                                          'contribution from team results.',
                               'Formula and example': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                      'Cp, Cpk and DPMO: state the context, your specific action, '
                                                      'supporting evidence and what you learned. For this formula '
                                                      'and example frame, distinguish your contribution from team '
                                                      'results.',
                               'Application': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk '
                                              'and DPMO: state the context, your specific action, supporting '
                                              'evidence and what you learned. For this application frame, '
                                              'distinguish your contribution from team results.',
                               'Limitations': '[SAMPLE TEMPLATE — replace with your verified experience] Cp, Cpk '
                                              'and DPMO: state the context, your specific action, supporting '
                                              'evidence and what you learned. For this limitations frame, '
                                              'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'l5': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] FMEA '
                                                 'and control plan: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this primary '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] FMEA and control plan: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] FMEA and '
                                             'control plan: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'a1': {'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] Excel practical readiness: state the '
                                                        'context, your specific action, supporting evidence and '
                                                        'what you learned. For this interview explanation frame, '
                                                        'distinguish your contribution from team results.',
                               'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified '
                                                            'experience] Excel practical readiness: state the '
                                                            'context, your specific action, supporting evidence '
                                                            'and what you learned. For this practical example or '
                                                            'code frame, distinguish your contribution from team '
                                                            'results.',
                               'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                   'Excel practical readiness: state the context, your specific '
                                                   'action, supporting evidence and what you learned. For this '
                                                   'project evidence frame, distinguish your contribution from '
                                                   'team results.',
                               'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                       'Excel practical readiness: state the context, your '
                                                       'specific action, supporting evidence and what you '
                                                       'learned. For this technical follow-ups frame, distinguish '
                                                       'your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'a2': {'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] SQL core queries: state the context, your '
                                                        'specific action, supporting evidence and what you '
                                                        'learned. For this interview explanation frame, '
                                                        'distinguish your contribution from team results.',
                               'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified '
                                                            'experience] SQL core queries: state the context, '
                                                            'your specific action, supporting evidence and what '
                                                            'you learned. For this practical example or code '
                                                            'frame, distinguish your contribution from team '
                                                            'results.',
                               'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] SQL '
                                                   'core queries: state the context, your specific action, '
                                                   'supporting evidence and what you learned. For this project '
                                                   'evidence frame, distinguish your contribution from team '
                                                   'results.',
                               'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                       'SQL core queries: state the context, your specific '
                                                       'action, supporting evidence and what you learned. For '
                                                       'this technical follow-ups frame, distinguish your '
                                                       'contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'a3': {'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] SQL intermediate concepts: state the '
                                                        'context, your specific action, supporting evidence and '
                                                        'what you learned. For this interview explanation frame, '
                                                        'distinguish your contribution from team results.',
                               'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified '
                                                            'experience] SQL intermediate concepts: state the '
                                                            'context, your specific action, supporting evidence '
                                                            'and what you learned. For this practical example or '
                                                            'code frame, distinguish your contribution from team '
                                                            'results.',
                               'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] SQL '
                                                   'intermediate concepts: state the context, your specific '
                                                   'action, supporting evidence and what you learned. For this '
                                                   'project evidence frame, distinguish your contribution from '
                                                   'team results.',
                               'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                       'SQL intermediate concepts: state the context, your '
                                                       'specific action, supporting evidence and what you '
                                                       'learned. For this technical follow-ups frame, distinguish '
                                                       'your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'a4': {'frames': {'Interview explanation': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] Power BI dashboard defence: state the '
                                                        'context, your specific action, supporting evidence and '
                                                        'what you learned. For this interview explanation frame, '
                                                        'distinguish your contribution from team results.',
                               'Practical example or code': '[SAMPLE TEMPLATE — replace with your verified '
                                                            'experience] Power BI dashboard defence: state the '
                                                            'context, your specific action, supporting evidence '
                                                            'and what you learned. For this practical example or '
                                                            'code frame, distinguish your contribution from team '
                                                            'results.',
                               'Project evidence': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                   'Power BI dashboard defence: state the context, your specific '
                                                   'action, supporting evidence and what you learned. For this '
                                                   'project evidence frame, distinguish your contribution from '
                                                   'team results.',
                               'Technical follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                       'Power BI dashboard defence: state the context, your '
                                                       'specific action, supporting evidence and what you '
                                                       'learned. For this technical follow-ups frame, distinguish '
                                                       'your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'a5': {'frames': {'60-second summary': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                    'One flagship analytics project: state the context, your '
                                                    'specific action, supporting evidence and what you learned. '
                                                    'For this 60-second summary frame, distinguish your '
                                                    'contribution from team results.',
                               'Detailed defence': '[SAMPLE TEMPLATE — replace with your verified experience] One '
                                                   'flagship analytics project: state the context, your specific '
                                                   'action, supporting evidence and what you learned. For this '
                                                   'detailed defence frame, distinguish your contribution from '
                                                   'team results.',
                               'My exact contribution': '[SAMPLE TEMPLATE — replace with your verified '
                                                        'experience] One flagship analytics project: state the '
                                                        'context, your specific action, supporting evidence and '
                                                        'what you learned. For this my exact contribution frame, '
                                                        'distinguish your contribution from team results.',
                               'Likely follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                    'One flagship analytics project: state the context, your '
                                                    'specific action, supporting evidence and what you learned. '
                                                    'For this likely follow-ups frame, distinguish your '
                                                    'contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'ai1': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                'Clarify your proficiency level: state the context, your specific '
                                                'action, supporting evidence and what you learned. For this short '
                                                'answer frame, distinguish your contribution from team results.',
                                'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                   'Clarify your proficiency level: state the context, your '
                                                   'specific action, supporting evidence and what you learned. '
                                                   'For this detailed answer frame, distinguish your contribution '
                                                   'from team results.',
                                'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                            'experience] Clarify your proficiency level: state '
                                                            'the context, your specific action, supporting '
                                                            'evidence and what you learned. For this evidence and '
                                                            'calculation frame, distinguish your contribution '
                                                            'from team results.',
                                'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Clarify your proficiency level: state the context, your '
                                                  'specific action, supporting evidence and what you learned. For '
                                                  'this follow-up bank frame, distinguish your contribution from '
                                                  'team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ai2': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] AI, '
                                                  'ML and GenAI distinctions: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'primary answer frame, distinguish your contribution from team '
                                                  'results.',
                                'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] AI, ML and GenAI distinctions: state the '
                                                          'context, your specific action, supporting evidence and '
                                                          'what you learned. For this example or application '
                                                          'frame, distinguish your contribution from team '
                                                          'results.',
                                'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] AI, ML '
                                              'and GenAI distinctions: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this follow-ups '
                                              'frame, distinguish your contribution from team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ai3': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] ML '
                                                  'workflow and evaluation: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'primary answer frame, distinguish your contribution from team '
                                                  'results.',
                                'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] ML workflow and evaluation: state the '
                                                          'context, your specific action, supporting evidence and '
                                                          'what you learned. For this example or application '
                                                          'frame, distinguish your contribution from team '
                                                          'results.',
                                'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] ML '
                                              'workflow and evaluation: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this follow-ups '
                                              'frame, distinguish your contribution from team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ai4': {'frames': {'60-second summary': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                     'Personal AI project defence: state the context, your '
                                                     'specific action, supporting evidence and what you learned. '
                                                     'For this 60-second summary frame, distinguish your '
                                                     'contribution from team results.',
                                'Detailed defence': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                    'Personal AI project defence: state the context, your '
                                                    'specific action, supporting evidence and what you learned. '
                                                    'For this detailed defence frame, distinguish your '
                                                    'contribution from team results.',
                                'My exact contribution': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Personal AI project defence: state the '
                                                         'context, your specific action, supporting evidence and '
                                                         'what you learned. For this my exact contribution frame, '
                                                         'distinguish your contribution from team results.',
                                'Likely follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                     'Personal AI project defence: state the context, your '
                                                     'specific action, supporting evidence and what you learned. '
                                                     'For this likely follow-ups frame, distinguish your '
                                                     'contribution from team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ac1': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Academic strengths: state the context, your specific action, '
                                                  'supporting evidence and what you learned. For this primary '
                                                  'answer frame, distinguish your contribution from team results.',
                                'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] Academic strengths: state the context, '
                                                          'your specific action, supporting evidence and what you '
                                                          'learned. For this example or application frame, '
                                                          'distinguish your contribution from team results.',
                                'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Academic '
                                              'strengths: state the context, your specific action, supporting '
                                              'evidence and what you learned. For this follow-ups frame, '
                                              'distinguish your contribution from team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ac2': {'frames': {'Short answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                'Academic learning in business: state the context, your specific '
                                                'action, supporting evidence and what you learned. For this short '
                                                'answer frame, distinguish your contribution from team results.',
                                'Detailed answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                   'Academic learning in business: state the context, your '
                                                   'specific action, supporting evidence and what you learned. '
                                                   'For this detailed answer frame, distinguish your contribution '
                                                   'from team results.',
                                'Evidence and calculation': '[SAMPLE TEMPLATE — replace with your verified '
                                                            'experience] Academic learning in business: state the '
                                                            'context, your specific action, supporting evidence '
                                                            'and what you learned. For this evidence and '
                                                            'calculation frame, distinguish your contribution '
                                                            'from team results.',
                                'Follow-up bank': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Academic learning in business: state the context, your '
                                                  'specific action, supporting evidence and what you learned. For '
                                                  'this follow-up bank frame, distinguish your contribution from '
                                                  'team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ac3': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Academic performance explanation: state the context, your '
                                                  'specific action, supporting evidence and what you learned. For '
                                                  'this primary answer frame, distinguish your contribution from '
                                                  'team results.',
                                'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] Academic performance explanation: state '
                                                          'the context, your specific action, supporting evidence '
                                                          'and what you learned. For this example or application '
                                                          'frame, distinguish your contribution from team '
                                                          'results.',
                                'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Academic '
                                              'performance explanation: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this follow-ups '
                                              'frame, distinguish your contribution from team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'ac4': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                  'Learning and improvement: state the context, your specific '
                                                  'action, supporting evidence and what you learned. For this '
                                                  'primary answer frame, distinguish your contribution from team '
                                                  'results.',
                                'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                          'experience] Learning and improvement: state the '
                                                          'context, your specific action, supporting evidence and '
                                                          'what you learned. For this example or application '
                                                          'frame, distinguish your contribution from team '
                                                          'results.',
                                'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Learning '
                                              'and improvement: state the context, your specific action, '
                                              'supporting evidence and what you learned. For this follow-ups '
                                              'frame, distinguish your contribution from team results.'},
                     'confidence': 0,
                     'done': False,
                     'notes': '',
                     'checks': []},
             'e1': {'frames': {'Primary answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Creative collaboration: state the context, your specific '
                                                 'action, supporting evidence and what you learned. For this '
                                                 'primary answer frame, distinguish your contribution from team '
                                                 'results.',
                               'Example or application': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Creative collaboration: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this example or application frame, '
                                                         'distinguish your contribution from team results.',
                               'Follow-ups': '[SAMPLE TEMPLATE — replace with your verified experience] Creative '
                                             'collaboration: state the context, your specific action, supporting '
                                             'evidence and what you learned. For this follow-ups frame, '
                                             'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'e2': {'frames': {'Concise answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Course learning: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this concise '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Learning and relevance': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Course learning: state the context, your '
                                                         'specific action, supporting evidence and what you '
                                                         'learned. For this learning and relevance frame, '
                                                         'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []},
             'e3': {'frames': {'Concise answer': '[SAMPLE TEMPLATE — replace with your verified experience] '
                                                 'Conference learning: state the context, your specific action, '
                                                 'supporting evidence and what you learned. For this concise '
                                                 'answer frame, distinguish your contribution from team results.',
                               'Learning and relevance': '[SAMPLE TEMPLATE — replace with your verified '
                                                         'experience] Conference learning: state the context, '
                                                         'your specific action, supporting evidence and what you '
                                                         'learned. For this learning and relevance frame, '
                                                         'distinguish your contribution from team results.'},
                    'confidence': 0,
                    'done': False,
                    'notes': '',
                    'checks': []}},
 'evidence': {'project': {'verified': False, 'notes': ''}, 'metric': {'verified': False, 'notes': ''}},
 'stories': [{'id': 'st0',
              'title': 'Leadership',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st1',
              'title': 'Achievement',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st2',
              'title': 'Failure',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st3',
              'title': 'Conflict',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st4',
              'title': 'Negotiation',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st5',
              'title': 'Data-driven decision',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st6',
              'title': 'Initiative',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'},
             {'id': 'st7',
              'title': 'Ethics',
              'source': 'your verified experience',
              'situation': '[COMPLETE: add your own verified situation; no invented incidents.]',
              'task': '[COMPLETE: add your own verified task; no invented incidents.]',
              'action': '[COMPLETE: add your own verified action; no invented incidents.]',
              'result': '[COMPLETE: add your own verified result; no invented incidents.]',
              'reflection': '[COMPLETE: add your own verified reflection; no invented incidents.]'}],
 'processes': [],
 'reviews': [],
 'generations': [],
 'settings': {'aiConsent': False, 'freeTierConfirmed': False}}

def initial_state():
    return deepcopy(_INITIAL)
