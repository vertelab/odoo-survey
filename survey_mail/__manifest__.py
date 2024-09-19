# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2023- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Survey: Mail",
    "version": "1.0",
    'summary': 'Adds better mail delivery',
    'description': """
    
    Bridge module adding UX requirements to ease mass mailing of survey attendees.
    
    """,
    'category': 'Sales',
    'license': 'AGPL-3',
    'author': 'Vertel AB',
    'maintainer': 'Vertel AB',
    'contributor': '',
    'website': "https://vertel.se/apps/odoo-survey/survey_mail",
    'images': ['/static/description/banner.png'], # 560x280 px.
    'repository': 'https://github.com/vertelab/odoo-survey',
    # Any module necessary for this one to work correctly
    
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
