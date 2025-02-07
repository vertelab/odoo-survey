# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2024- Vertel AB (<https://vertel.se>).
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
    'name': 'Survey: Website',
    'version': '18.0.1.0.0',
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
    'images': ['/static/description/banner.png'],  # 560x280 px.
    'repository': 'https://github.com/vertelab/odoo-survey',
    # Any module necessary for this one to work correctly

    "depends": ['survey', 'portal'],
    'data': [
        'views/survey_survey_view.xml',
        'views/survey_templates.xml',
    ],
    'assets': {
        'survey.survey_assets': [
            ('after', 'survey/static/src/scss/survey_templates_form.scss', 'survey_website/static/src/scss/survey_templates_form.scss'),
            # ('after', 'survey/static/src/js/survey_form.js', 'survey_website/static/src/js/survey_form.js'),
        ],

    },
    "installable": True,
    "auto_install": False,
}
