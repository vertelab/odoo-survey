from bs4 import BeautifulSoup

from markupsafe import Markup
import re
import werkzeug.urls

from odoo import fields, models
from odoo.tools.misc import file_open


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    def _prepare_mail_values(self, res_ids):
        """ When being in mass mailing mode, add 'mailing.trace' values directly
        in the o2m field of mail.mail. """
        mail_values_all = super()._prepare_mail_values(res_ids)

        # use only for allowed models in mass mailing
        if (self.composition_mode != 'mass_mail' or
            not self.mass_mailing_id or
            not self.model_is_thread):
            return mail_values_all

        trace_values_all = self._prepare_mail_values_mailing_traces(mail_values_all)
        with file_open("mass_mailing/static/src/scss/mass_mailing_mail.scss", "r") as fd:
            styles = fd.read()
        for res_id, mail_values in mail_values_all.items():
            body_html = mail_values['body_html']
            if mail_values.get('body_html'):
                if self.mass_mailing_id.mailing_model_id.model == 'survey.user_input':
                    full_body_soup = BeautifulSoup(body_html, 'html.parser')
                    survey_href = full_body_soup.find('a', id='survey_button_url')
                    if survey_href:
                        survey_record = self.env['survey.user_input'].browse(res_id)
                        utm_source = self.mass_mailing_id.source_id.name
                        utm_medium = self.mass_mailing_id.medium_id.name
                        answer_token = survey_record.access_token
                        survey_start_url = survey_record.survey_start_url
                        survey_url = (f'{survey_start_url}?answer_token={answer_token}'
                                      f'&utm_source={utm_source}&utm_medium={utm_medium}')
                        survey_href['href'] = survey_url
                    body_html = Markup(full_body_soup)

                body = self.env['ir.qweb']._render(
                    'mass_mailing.mass_mailing_mail_layout',
                    {'body': body_html, 'mailing_style': Markup(f'<style>{styles}</style>')},
                    minimal_qcontext=True,
                    raise_if_not_found=False
                )
                if body:
                    mail_values['body_html'] = body

            mail_values.update({
                'mailing_id': self.mass_mailing_id.id,
                'mailing_trace_ids': [(0, 0, trace_values_all[res_id])] if res_id in trace_values_all else False,
            })
        return mail_values_all
