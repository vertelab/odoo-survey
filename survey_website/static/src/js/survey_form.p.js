// #if VERSION == "16.0"
odoo.define('survey_website.form', function (require) {
    'use strict';

    var SurveyFormWidget = require('survey.form');

    SurveyFormWidget.include({
        /**
         * Handle keyboard navigation:
         * - 'enter' or 'arrow-right' => submit form
         * - 'arrow-left' => submit form (but go back backwards)
         * - other alphabetical character ('a', 'b', ...)
         *   Select the related option in the form (if available)
         *
         * @param {Event} event
         */
        _onKeyDown: function (event) {
            var self = this;
            var keyCode = event.keyCode;

            // If user is answering a text input, do not handle keydown
            // CTRL+enter will force submission (meta key for Mac)
            if ((this.$("textarea").is(":focus") || this.$('input').is(':focus')) &&
                (!(event.ctrlKey || event.metaKey) || keyCode !== 13)) {
                return;
            }
            // If in session mode and question already answered, do not handle keydown
            if (this.$('fieldset[disabled="disabled"]').length !== 0) {
                return;
            }
            // Disable all navigation keys when zoom modal is open, except the ESC.
            if ((this.imgZoomer && !this.imgZoomer.isDestroyed()) && keyCode !== 27) {
                return;
            }

            var letter = String.fromCharCode(keyCode).toUpperCase();

            // Handle Start / Next / Submit
            if (keyCode === 13 || keyCode === 39) {  // Enter or arrow-right: go Next
                event.preventDefault();
                if (!this.preventEnterSubmit) {
                    var isFinish = this.$('button[value="finish"]').length !== 0;
                    this._submitForm({isFinish: isFinish});
                }
            } else if (keyCode === 37) {  // arrow-left: previous (if available)
                // It's easier to actually click on the button (if in the DOM) as it contains necessary
                // data that are used in the event handler.
                // Again, global selector necessary since the navigation is outside of the form.
                $('.o_survey_navigation_submit[value="previous"]').click();
            } else if (self.options.questionsLayout === 'page_per_question'
                       && letter.match(/[a-z]/i)) {
                var $choiceInput = this.$(`input[data-selection-key=${letter}]`);
                if ($choiceInput.length === 1) {
                    $choiceInput.prop("checked", !$choiceInput.prop("checked")).trigger('change');

                    // Avoid selection key to be typed into the textbox if 'other' is selected by key

                    /**********************************************************
                      commented out with the hope of no issues,
                      This will allow survey editor update text without any keyboard limitations.
                      TODO: SmartPeople Fixme - cleaner solution? be my guest!
                     **********************************************************/
                    // event.preventDefault();
                }
            }
        },
    })
})

// #endif