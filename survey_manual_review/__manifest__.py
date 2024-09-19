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
    "name": "Survey: Manual Review",
    "version": "1.0.0",
    'summary': 'Make it so that one can case by case give a passing grade to an survey.',
    'description': """
Make it so that one can case by case give a passing grade to an survey.
Useful when you have an open question that a person has to read before marking it as correct.
    """,

    'category': 'Sales',
    'license': 'AGPL-3',
    'author': 'Vertel AB',
    'maintainer': 'Vertel AB',
    'contributor': '',
    'website': "https://vertel.se/apps/odoo-survey/survey_manual_review",
    'images': ['/static/description/banner.png'], # 560x280 px.
    'repository': 'https://github.com/vertelab/odoo-survey',
    # Any module necessary for this one to work correctly
        
    "depends": ['survey','website_slides','website_slides_survey'],
    'data': [
        'views/survey_view.xml',
   ],
    "installable": True,
    "auto_install": False,
}
