import logging
from markupsafe import Markup
from jinja2 import Template
from odoo.addons.survey.controllers.main import Survey

_logger = logging.getLogger(__name__)


class SurveyExtended(Survey):

    def _prepare_survey_data(self, survey_sudo, answer_sudo, **post):
        data = super()._prepare_survey_data(survey_sudo, answer_sudo, **post)
        template = Template(survey_sudo.description)
        context = {
            "object": survey_sudo,  # Pass survey as "object"
        }
        data['description'] = Markup(template.render(context))
        return data
