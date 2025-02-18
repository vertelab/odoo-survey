from odoo import models, fields, api, _


class LikertScaleTemplate(models.Model):
    _name = 'likert.scale.template'

    name = fields.Char(string="Name")
    option_ids = fields.One2many('likert.scale.template.options', 'template_id')


class LikertScaleTemplateOptions(models.Model):
    _name = 'likert.scale.template.options'

    option = fields.Char(string="Option")
    score = fields.Char(string="Score")
    sequence = fields.Integer("Sequence")
    template_id = fields.Many2one('likert.scale.template', string="Template")