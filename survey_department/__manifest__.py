# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2019-2024 Vertel AB (<http://vertel.se>).
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Survey Department',
    'version': '17.0',
    'category': 'survey',
    'license': 'AGPL-3',
    'summary': 'Add department on surveys',
    'description': """
        * Add department on survey
        * My department filter
        * My serveys filter
        * Department grouping, search
        
        """,
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['survey', 'hr',],
    'data': [
        'views/survey_views.xml',
#        'security/survey_security.xml'
    ],
    'installable': True,
    'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
