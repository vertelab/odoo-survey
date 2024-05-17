# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import textwrap
import uuid

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_is_zero

_logger = logging.getLogger(__name__)
import werkzeug


class SurveyUserInput(models.Model):
    """ Metadata for a set of one user's answers to a particular survey """
    _inherit = "survey.user_input"
    _mailing_enabled = True

    @api.depends('survey_id.access_token')
    def _compute_survey_start_url(self):
        for invite in self:
            invite.survey_start_url = werkzeug.urls.url_join(
                invite.survey_id.get_base_url(), invite.survey_id.get_start_url()
            ) if invite.survey_id else False

    survey_start_url = fields.Char('Survey URL', readonly=True, compute='_compute_survey_start_url')

    def _mailing_get_default_domain(self, mailing):
        return [('state', '!=', 'cancel')]
