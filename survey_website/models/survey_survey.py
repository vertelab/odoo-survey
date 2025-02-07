from random import randint
from odoo import models, fields, api

COLOR_MAPPING = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "lightblue",
    5: "darkpurple",
    6: "salmon",
    7: "mediumblue",
    8: "darkblue",
    9: "fuchsia",
    10: "green",
    11: "purple",
}


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    # _inherit = ['survey.survey', 'portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    def get_color(self):
        return COLOR_MAPPING.get(self.color, "black")

    def action_preview_custom_survey(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'name': "Custom Test Survey",
            'target': 'new',
            'url': '/custom_survey/test/%s' % self.access_token,
        }


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    def get_color(self):
        return COLOR_MAPPING.get(self.color, "black")

    color = fields.Integer(default=lambda dummy: randint(1, 11))


class SurveyQuestionAnswer(models.Model):
    _inherit = 'survey.question.answer'

    def get_color(self):
        return COLOR_MAPPING.get(self.color, "black")

    color = fields.Integer(default=lambda dummy: randint(1, 11))
