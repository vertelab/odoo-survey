{
    "name": "Survey Likert Scale",
    "version": "17.0.1.0.0",
    'summary': 'Adds Likert Scale',
    'category': 'Survey',
    'description': """
Template for Likert Scale.
    """,
    "author": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://github.com/vertelab/odoo-survey",
    "depends": ['survey'],
    'data': [
        'security/ir.model.access.csv',
        'views/likert_scale_view.xml',
        'views/survey_question_view.xml',
   ],
    "installable": True,
    "auto_install": False,
}
