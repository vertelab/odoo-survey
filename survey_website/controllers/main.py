# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
import werkzeug

from collections import defaultdict
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import fields, http, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.http import request, content_disposition
from odoo.osv import expression
from odoo.tools import format_datetime, format_date, is_html_empty
from odoo.addons.survey.controllers.main import Survey
from odoo.addons.base.models.ir_qweb import keep_query

_logger = logging.getLogger(__name__)

