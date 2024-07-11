{
    "name": "Survey Manual Review",
    "version": "17.0.1.0.0",
    'summary': 'Make it so that one can case by case give a passing grade to an survey.',
    'category': 'Survey',
    'description': """
Make it so that one can case by case give a passing grade to an survey.
Useful when you have an open question that a person has to read before marking it as correct.
    """,
    "author": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://github.com/vertelab/odoo-survey",
    "depends": ['survey','website_slides','website_slides_survey'],
    'data': [
        'views/survey_view.xml',
   ],
    "installable": True,
    "auto_install": False,
}
