{
    "name": "Survey Template",
    "version": "17.0.1.0.0",
    'summary': 'Adds better template handling ',
    'category': 'Survey',
    'description': """

    Define templates and join those with surveys

    """,
    "author": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://github.com/vertelab/odoo-survey",
    "depends": ['survey',],
    'data': [
        'data/survey_data.xml',
        'views/survey_view.xml',
       ],
    "installable": True,
    "auto_install": False,
}
