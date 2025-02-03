# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP,  Open Source Management Solution,  third party addon
#    Copyright (C) 2024 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation,  either version 3 of the
#    License,  or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not,  see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
import random
import threading

from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools
from odoo.tools import exception_to_unicode
from odoo.tools.translate import _
from odoo.exceptions import MissingError, ValidationError, UserError

_logger = logging.getLogger(__name__)


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    is_template = fields.Boolean(string='Is Template')
    display_name = fields.Char('Name', compute='_compute_display_name', readonly=True)

    def _compute_display_name(self):
        """ Onchange results in product.display_name not being directly accessible """
        for survey in self:
            if survey.is_template:
                survey.display_name = _("[TEMPLATE] %s" % survey.title)
            else:
                survey.display_name = survey.title

    def new_from_template(self):
        new_template = self.copy()
        new_template.is_template = False
        return {  # Open the new survey
            'name': 'Survey',
            'type': 'ir.actions.act_window',
            'res_model': 'survey.survey',
            'view_mode': 'form',
            'res_id': new_template.id,
            'target': 'current',
            'context': {
            },
        }

    def action_join(self, survey_ids):
        main_survey = survey_ids.filtered(lambda s: not s.is_template)
        if len(main_survey) == 1:
            main_survey = main_survey[0]
        elif len(main_survey) > 1:
            raise UserError(_(f"More than one non template"))
        elif not main_survey:
            raise UserError(_(f"Non template is missing"))
        for survey in survey_ids:
            if survey.id != main_survey.id:
                tmp = survey.copy()
                main_survey.question_and_page_ids = main_survey.question_and_page_ids + tmp.question_and_page_ids
                tmp.unlink()
        return {
            'name': 'Survey',
            'type': 'ir.actions.act_window',
            'res_model': 'survey.survey',
            'view_mode': 'form',
            'res_id': main_survey.id,
            'target': 'current',
        }
