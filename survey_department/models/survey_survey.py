# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2019- Vertel AB (<http://vertel.se>).
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

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class Survey(models.Model):
    _inherit = 'survey.survey'

    def _default_department_ids(self):
        return self.env.user.employee_ids.mapped('department_id')

    department_id = fields.Many2one(comodel_name='hr.department', string='Department', default=_default_department_ids)


class HRDepartment(models.Model):
    _inherit = 'hr.department'

    user_ids = fields.Many2many(comodel_name='res.users', string='Users', help="Users in this department",
                                compute="_user_ids", store=True)

    @api.depends('member_ids', 'manager_id')
    def _user_ids(self):
        for rec in self:
            rec.user_ids = rec.member_ids.mapped('user_id') + rec.member_ids.child_ids.mapped(
                'user_id') + rec.manager_id.mapped('user_id')


class Users(models.Model):
    _inherit = 'res.users'

    def _default_department_ids(self):
        # ~ _logger.warn('\n\n_default_departments_ids\n%s\n' % self.env.context)	
        return self.env.user.employee_ids.mapped('department_id')

    department_ids = fields.Many2many(comodel_name='hr.department', string='Department',
                                      default=_default_department_ids)
