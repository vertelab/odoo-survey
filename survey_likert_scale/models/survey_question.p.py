from odoo import models, fields, api, Command


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    is_likert_scale = fields.Boolean(string="Likert Scale")
    likert_scale_template_id = fields.Many2one('likert.scale.template', string="Likert Scale Template")

    @api.onchange('likert_scale_template_id')
    def onchange_likert_scale_template(self):
        if self.likert_scale_template_id:
            if self.suggested_answer_ids:
                self.write({'suggested_answer_ids': [Command.clear()]})

            self.write({
                'suggested_answer_ids': [
                    Command.create({
                        'value': template_option.option,
                        'answer_score': template_option.score
                    })
                    for template_option in self.likert_scale_template_id.option_ids]
            })
