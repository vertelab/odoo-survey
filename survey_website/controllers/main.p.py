import logging
from markupsafe import Markup
from jinja2 import Template
from odoo.addons.survey.controllers.main import Survey
from odoo.http import request, content_disposition

_logger = logging.getLogger(__name__)


class SurveyExtended(Survey):

    def _prepare_survey_data(self, survey_sudo, answer_sudo, **post):
        data = super()._prepare_survey_data(survey_sudo, answer_sudo, **post)

        survey = data.get('survey')
        answer = data.get('answer')
        question = data.get('question')

        survey_description = Template(survey_sudo.description)
        question_description = "<div></div>"

        if question and question.description:
            question_description = Template(question.description)

        context = {
            # "object": data,

            "answer": answer,
            "survey": survey,
            "user_id": request.env.user,
        }
        data['survey_description'] = Markup(survey_description.render(context))
        if question and question.description:
            data['question_description'] = Markup(question_description.render(context))

        return data
