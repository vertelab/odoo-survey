{
    "name": "Survey Mail",
    "version": "17.0.1.0.0",
    'summary': 'Adds better mail delivery',
    'category': 'Survey',
    'description': """
Bridge module adding UX requirements to ease mass mailing of survey attendees.

    """,
    "author": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://github.com/vertelab/odoo-survey",
    "depends": ['survey','barcodes', 'base_setup', 'mail', 'phone_validation', 'portal', 'utm'],
    'data': [
        'views/survey_mail.xml',
       ],
    "installable": True,
    "auto_install": False,
}
