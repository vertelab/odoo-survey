#-*- coding: utf-8 -*-
##############################################################################
#
#   Odoo SA, Open Source Management Solution, third party addon
#   Copyright (C) 2024- Vertel AB (<https://vertel.se>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Survey: Embed Survey on Other Websites',
    'version': '1.0',
    'summary': 'Adds odoo survey on other websites ',
    'description': """
        Embed Survey on Other Websites
    """,
    'category': 'Survey',
    'license': 'AGPL-3',
    'author': 'Vertel AB',
    'maintainer': 'Vertel AB',
    'contributor': '',
    'website': "https://vertel.se/apps/odoo-survey/survey_template",
    'images': ['/static/description/banner.png'],  # 560x280 px.
    'repository': 'https://github.com/vertelab/odoo-survey',
    # Any module necessary for this one to work correctly
    "depends": ['survey', ],
    'data': [
        'views/survey_survey_view.xml',
        # 'views/survey_templates.xml',
        "views/survey_website_pop_templates.xml",
    ],
    'assets': {
    #     'survey.survey_assets': [
    #         ('after', 'survey/static/src/scss/survey_templates_form.scss', 'survey_website/static/src/scss/survey_templates_form.scss'),
    #         ('after', 'survey/static/src/js/survey_form.js', 'survey_website/static/src/js/survey_form.js'),
    #     ],
        # Bundle of External Libraries of the Survey (Odoo + required modules)
        'survey_website_popup.external_lib': [
            # Momentjs
            'web/static/lib/moment/moment.js',
            'web/static/lib/luxon/luxon.js',
            # Odoo minimal lib
            'web/static/lib/underscore/underscore.js',
            'web/static/lib/underscore.string/lib/underscore.string.js',
            # jQuery
            'web/static/lib/jquery/jquery.js',
            'web/static/lib/jquery.ui/jquery-ui.js',
            'web/static/lib/jquery/jquery.browser.js',
            'web/static/lib/jquery.ba-bbq/jquery.ba-bbq.js',
            # Qweb2 lib
            'web/static/lib/qweb/qweb2.js',
            # Odoo JS Framework
            'web/static/src/legacy/js/promise_extension.js',
            'web/static/src/boot.js',
            'web/static/lib/owl/owl.js',
            'web/static/lib/owl/odoo_module.js',
            'web/static/src/owl2_compatibility/*.js',
            'web/static/src/legacy/legacy_component.js',
            'web/static/src/core/browser/browser.js',
            'web/static/src/core/browser/feature_detection.js',
            'web/static/src/core/dialog/dialog.js',
            'web/static/src/core/errors/error_dialogs.js',
            'web/static/src/core/effects/**/*.js',
            'web/static/src/core/hotkeys/hotkey_service.js',
            'web/static/src/core/hotkeys/hotkey_hook.js',
            'web/static/src/core/l10n/dates.js',
            'web/static/src/core/l10n/localization.js',
            'web/static/src/core/l10n/localization_service.js',
            'web/static/src/core/l10n/translation.js',
            'web/static/src/core/main_components_container.js',
            'web/static/src/core/network/rpc_service.js',
            'web/static/src/core/assets.js',
            'web/static/src/core/notifications/notification.js',
            'web/static/src/core/notifications/notification_container.js',
            'web/static/src/core/notifications/notification_service.js',
            'web/static/src/core/registry.js',
            'web/static/src/core/transition.js',
            'web/static/src/core/ui/block_ui.js',
            'web/static/src/core/ui/ui_service.js',
            'web/static/src/core/user_service.js',
            'web/static/src/core/utils/components.js',
            'web/static/src/core/utils/functions.js',
            'web/static/src/core/utils/hooks.js',
            'web/static/src/core/utils/numbers.js',
            'web/static/src/core/utils/strings.js',
            'web/static/src/core/utils/timing.js',
            'web/static/src/core/utils/ui.js',
            'web/static/src/env.js',
            'web/static/src/legacy/utils.js',
            'web/static/src/legacy/js/owl_compatibility.js',
            'web/static/src/legacy/js/libs/download.js',
            'web/static/src/legacy/js/libs/content-disposition.js',
            'web/static/src/legacy/js/libs/pdfjs.js',
            'web/static/src/legacy/js/services/config.js',
            'web/static/src/legacy/js/core/abstract_service.js',
            'web/static/src/legacy/js/core/class.js',
            'web/static/src/legacy/js/core/collections.js',
            'web/static/src/legacy/js/core/translation.js',
            'web/static/src/legacy/js/core/ajax.js',
            'im_livechat/static/src/js/ajax_external.js',
            'web/static/src/legacy/js/core/time.js',
            'web/static/src/legacy/js/core/mixins.js',
            'web/static/src/legacy/js/core/service_mixins.js',
            'web/static/src/legacy/js/core/rpc.js',
            'web/static/src/legacy/js/core/widget.js',
            'web/static/src/legacy/js/core/registry.js',
            'web/static/src/session.js',
            'web/static/src/legacy/js/core/session.js',
            'web/static/src/legacy/js/core/concurrency.js',
            'web/static/src/legacy/js/core/cookie_utils.js',
            'web/static/src/legacy/js/core/utils.js',
            'web/static/src/legacy/js/core/minimal_dom.js',
            'web/static/src/legacy/js/core/dom.js',
            'web/static/src/legacy/js/core/qweb.js',
            'web/static/src/legacy/js/core/bus.js',
            'web/static/src/legacy/js/services/core.js',
            'web/static/src/legacy/js/core/local_storage.js',
            'web/static/src/legacy/js/core/ram_storage.js',
            'web/static/src/legacy/js/core/abstract_storage_service.js',
            'web/static/src/legacy/js/common_env.js',
            'web/static/src/legacy/js/public/lazyloader.js',
            'web/static/src/legacy/js/public/public_env.js',
            'web/static/src/legacy/js/public/public_root.js',
            'web/static/src/legacy/js/public/public_root_instance.js',
            'web/static/src/legacy/js/public/public_widget.js',
            'web/static/src/legacy/js/services/ajax_service.js',
            'web/static/src/legacy/js/services/local_storage_service.js',
            # Bus, Mail, Livechat
            'bus/static/src/im_status_service.js',
            'bus/static/src/multi_tab_service.js',
            'bus/static/src/services/bus_service.js',
            'bus/static/src/services/legacy/make_bus_service_to_legacy_env.js',
            'bus/static/src/workers/websocket_worker.js',
            'bus/static/src/workers/websocket_worker_utils.js',
            'mail/static/src/js/utils.js',
            # 'im_livechat/static/src/legacy/public_livechat_chatbot.js',

            ('include', 'web._assets_helpers'),

            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            # 'im_livechat/static/src/scss/im_livechat_bootstrap.scss',
            # 'im_livechat/static/src/legacy/public_livechat.scss',
            # 'im_livechat/static/src/legacy/public_livechat_chatbot.scss',

            'web/static/src/core/utils/transitions.scss',

            'mail/static/src/utils/*.js',
            'mail/static/src/js/emojis.js',
            'mail/static/src/component_hooks/*.js',
            # ('include', 'im_livechat.assets_public_livechat'),
            'mail/static/src/services/messaging_service.js',
            # Framework JS
            'bus/static/src/*.js',
            'bus/static/src/services/presence_service.js',
            'web/static/lib/luxon/luxon.js',
            'web/static/src/core/**/*',
            # FIXME: debug menu currently depends on webclient, once it doesn't we don't need to remove the contents of the debug folder
            ('remove', 'web/static/src/core/debug/**/*'),
            'web/static/src/env.js',
            'web/static/src/legacy/js/core/dialog.js',
            'web/static/src/legacy/js/core/owl_dialog.js',
            'web/static/src/legacy/js/core/misc.js',
            'web/static/src/legacy/js/fields/field_utils.js',
        ]
    },
    "installable": True,
    "auto_install": False,
}
