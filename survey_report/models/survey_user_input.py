from odoo import fields, models, tools, api
import random


class SurveySurvey(models.Model):
    _inherit = "survey.survey"

    @api.model
    def generate_random_number(self, range_from, range_to):
        return random.randint(range_from, range_to)


class SurveyInput(models.Model):
    _inherit = "survey.user_input.line"

    question_text = fields.Char(string="Question Text", related="question_id.title", store=True)

    answer_score_average = fields.Float(string="Average Score", related="answer_score", store=True,
                                        aggregator="avg")
    value_numerical_box_average = fields.Float(
        string="Average Numerical answer", related="value_numerical_box", store=True, aggregator="avg")

    answer_score_min = fields.Float(string="Minimum Score", related="answer_score", store=True, aggregator="min")
    value_numerical_box_min = fields.Float(
        string="Minimum Numerical answer", related="value_numerical_box", store=True, aggregator="min")

    answer_score_max = fields.Float(string="Maximum Score", related="answer_score", store=True, aggregator="max")
    value_numerical_box_max = fields.Float(
        string="Maximum Numerical answer", related="value_numerical_box", store=True, aggregator="max")
