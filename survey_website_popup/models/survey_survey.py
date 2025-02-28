from odoo import models, fields, api


class Survey(models.Model):
    _inherit = "survey.survey"

    delay = fields.Integer(string="Delay (sec)", default=100)

    def _compute_script_external(self):
        values = {
            "dbname": self._cr.dbname,
        }
        for record in self:
            values["survey_token"] = self.access_token
            values["url"] = record.get_base_url()
            record.script_external = self.env['ir.qweb']._render(
                'survey_website_popup.external_loader', values
            ) if record.id else False

    script_external = fields.Char(string="", compute=_compute_script_external)

