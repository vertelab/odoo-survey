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
    "depends": ['survey', 'barcodes', 'base_setup', 'mail', 'phone_validation', 'portal', 'utm', 'mass_mailing'],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_mail.xml',
        'views/survey_survey_view.xml',
        'wizard/survery_participant_invite_view.xml',
        'views/survey_user_input_view.xml',
        # 'views/mailing_mailing_view.xml',
        'data/ir_cron_data.xml',
        # 'views/survey_question_view.xml',

        # Snippets
        'views/snippets/s_survey_button.xml',
        'views/mass_mailing_templates.xml',
   ],
    "installable": True,
    "auto_install": False,
}
