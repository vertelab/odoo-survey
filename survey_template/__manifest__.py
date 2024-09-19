{
    "name": "Survey: Template",
    "version": "17.0.1.0.0",
    'summary': 'Adds better template handling ',
    'description': """

    Define templates and join those with surveys

    """,

    'category': 'Sales',
    'license': 'AGPL-3',
    'author': 'Vertel AB',
    'maintainer': 'Vertel AB',
    'contributor': '',
    'website': "https://vertel.se/apps/odoo-survey/survey_template",
    'images': ['/static/description/banner.png'], # 560x280 px.
    'repository': 'https://github.com/vertelab/odoo-survey',
    # Any module necessary for this one to work correctly
    
    "depends": ['survey',],
    'data': [
        'data/survey_data.xml',
        'views/survey_view.xml',
       ],
    "installable": True,
    "auto_install": False,
}
