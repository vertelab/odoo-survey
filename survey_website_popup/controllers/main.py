# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug.exceptions import NotFound

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.base.models.assetsbundle import AssetsBundle
from odoo.addons.survey.controllers.main import Survey


class SurveyWebsiteController(Survey):

    @http.route('/survey/<string:survey_token>/popup', type='http', auth='public', cors="*")
    def serve_survey_popup(self, survey_token, answer_token=None):
        answer_from_cookie = False
        if not answer_token:
            answer_token = request.httprequest.cookies.get('survey_%s' % survey_token)
            answer_from_cookie = bool(answer_token)

        access_data = self._get_access_data(survey_token, answer_token, ensure_token=False)

        survey_sudo = access_data['survey_sudo']

        if not survey_sudo:
            return request.not_found()

        survey_url = f"http://localhost:8069/survey/start/{survey_token}"

        js_code = f"""
            (function() {{
                function showSurveyPopup() {{
                    let modal = document.createElement("div");
                    modal.innerHTML = `
                        <div id="survey-popup" style="position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); display:flex; justify-content:center; align-items:center; z-index:1000;">
                            <div style="background:white; padding:10px; border-radius:5px; width:70%; position:relative;">
                                <iframe src="{survey_url}" style="width:100%; height:700px; border:none;"></iframe>
                                <button id="close-survey" style="position:absolute; top:10px; right:10px;">✖</button>
                            </div>
                        </div>
                    `;
                    document.body.appendChild(modal);
                    document.getElementById("close-survey").onclick = function () {{
                        modal.remove();
                    }};
                }}

                if ({survey_sudo.id}) {{
                    setTimeout(showSurveyPopup, {survey_sudo.delay});
                }}
            }})();
            """

        return request.make_response(js_code, headers=[('Content-Type', 'application/javascript')])
