from random import randint
from odoo import models, fields, api


COLOR_MAPPING = {
    1: "#F06050",
    2: "#F4A460",
    3: "#F7CD1F",
    4: "#6CC1ED",
    5: "#814968",
    6: "#EB7E7F",
    7: "#2C8397",
    8: "#475577",
    9: "#D6145F",
    10: "#30C381",
    11: "#9365B8",
}


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    def get_color(self):
        return COLOR_MAPPING.get(self.color, "black")


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
