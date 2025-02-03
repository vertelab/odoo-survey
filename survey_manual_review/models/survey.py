from odoo import models, fields, api, Command


class SlideChannel(models.Model):
    _inherit = 'slide.channel'
    surveys_manual_review = fields.Many2many('survey.user_input', string="Needs Manual Review",
                                             compute="compute_surveys_manual_review")
    surveys_manual_review_count = fields.Integer(compute="compute_surveys_manual_review")

    def compute_surveys_manual_review(self):
        for record in self:
            surveys = self.env['survey.user_input'].search(
                [('slide_id.channel_id', '=', record.id), ('manually_reviewed', '=', False)])
            record.surveys_manual_review = surveys
            record.surveys_manual_review_count = len(surveys)

    def action_show_surveys(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Surveys',
            'res_model': 'survey.user_input',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('manually_reviewed', '=', False), ('id', 'in', self.surveys_manual_review.ids)],
            'context': {},
        }


class Survey(models.Model):
    _inherit = 'survey.survey'
    needs_manual_review = fields.Boolean(string="Needs Manual Review")


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'
    needs_manual_review = fields.Boolean(related='survey_id.needs_manual_review')
    manually_reviewed = fields.Boolean('Manually Reviewed', tracking=True, readonly=True)

    def mark_manual_done(self):
        self.manually_reviewed = True
