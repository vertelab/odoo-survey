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
from odoo.exceptions import MissingError, ValidationError


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


    def action_join(self,survey_ids):
        main_survey = survey_ids.filtered(lambda s: s.is_template == False)
        if len(main_survey)>1:
            main_survey = main_survey[0]
        elif not main_survey:
            raise UserError(_(f"Non template is missing"))
        for survey in survey_ids:
            if survey.id != main_survey.id:
                main_survey = survey.copy()
                # ~ for q in survey.question_and_page_ids:
                    # ~ main_survey.question_and_page_ids = (0, 0, { # survey.question
                        # ~ 'title': q.title,
                        # ~ 'question_type': q.question_type,
                        # ~ 'suggested_answer_ids': [(0, 0, { # survey.question.answer
                                # ~ 'value': a.value,
                                # ~ 'is_correct': a.is_correct,
                                # ~ 'answer_score': a.answer_score,
                            # ~ }) for a in q.suggested_answer_ids]
                        # ~ })
        return {  # Open the new survey
            'name': 'Survey',
            'type': 'ir.actions.act_window',
            'res_model': 'survey.survey',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                # ~ 'default_survey_model_id': self.env.ref('survey.model_survey_registration').id,
                # ~ 'default_mailing_domain': repr([('survey_id', 'in', self.ids), ('state', '!=', 'cancel')])
            },
        }
