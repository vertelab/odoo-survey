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

    answer_score_average = fields.Float(string="Average Score", related="answer_score", store=True, group_operator="avg")
    value_numerical_box_average = fields.Float(
        string="Average Numerical answer", related="value_numerical_box", store=True, group_operator="avg")

    answer_score_min = fields.Float(string="Minimum Score", related="answer_score", store=True, group_operator="min")
    value_numerical_box_min = fields.Float(
        string="Minimum Numerical answer", related="value_numerical_box", store=True, group_operator="min")

    answer_score_max = fields.Float(string="Maximum Score", related="answer_score", store=True, group_operator="max")
    value_numerical_box_max = fields.Float(
        string="Maximum Numerical answer", related="value_numerical_box", store=True, group_operator="max")
    # answer_score_avg = fields.Float(string="Score Avg", store=True, group_operator="avg")

    # def _from(self):
    #     return """
    #         FROM survey_user_input_line user_input_line
    #         JOIN survey_user_input user_input ON user_input_line.user_input_id = user_input.id
    #         JOIN survey_question question ON user_input_line.question_id = question.id
    #     """
    #
    # def _where(self):
    #     return """
    #         WHERE user_input_line.answer_score IS NOT NULL
    #     """
    #
    # def _group_by(self):
    #     group_by_str = """
    #         GROUP BY
    #             user_input_line.user_input_id,
    #             user_input.survey_id
    #     """
    #     return group_by_str
    #
    # def _select(self):
    #     select_str = """
    #         SELECT
    #             user_input.survey_id,
    #             sum(user_input_line.answer_score) / count(*) as answer_score_avg
    #     """
    #     return select_str
    #
    # @property
    # def _table_query(self):
    #     return '%s %s %s %s' % (self._select(), self._from(), self._where(), self._group_by())
