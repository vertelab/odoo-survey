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

    date_begin = fields.Date(string='Date Begin') # fields.date.add|context_today|end_of|start_of|substract|to_date|to_string|today
    date_end   = fields.Date(string='Date End') # fields.date.add|context_today|end_of|start_of|substract|to_date|to_string|today
