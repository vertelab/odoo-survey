/** @odoo-module **/

import SurveyFormWidget  from "@survey/js/survey_form";

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

        if (['one_page', 'page_per_section'].includes(self.options.questionsLayout) && !self.options.isStartScreen) {
            if (this.$("input").is(":focus") && event.key === "Enter") {
                event.preventDefault();
            }
            if (!(event.ctrlKey || event.metaKey) || event.key !== "Enter") {
                return;
            }
        }

        // If user is answering a text input, do not handle keydown
        // CTRL+enter will force submission (meta key for Mac)
        if ((this.$("textarea").is(":focus") || this.$('input').is(':focus')) &&
            (!(event.ctrlKey || event.metaKey) || event.key !== "Enter")) {
            return;
        }
        // If in session mode and question already answered, do not handle keydown
        if (this.$('fieldset[disabled="disabled"]').length !== 0) {
            return;
        }
        // Disable all navigation keys when zoom modal is open, except the ESC.
        if ((this.imgZoomer && !this.imgZoomer.isDestroyed()) && event.key !== "Escape") {
            return;
        }

        var letter = event.key.toUpperCase();

        // Handle Start / Next / Submit
        if (event.key === "Enter" || event.key === "ArrowRight") {  // Enter or arrow-right: go Next
            event.preventDefault();
            if (!this.preventEnterSubmit) {
                this._submitForm({
                    isFinish: this.el.querySelectorAll('button[value="finish"]').length !== 0,
                    nextSkipped: this.el.querySelectorAll('button[value="next_skipped"]').length !== 0 ? event.key === "Enter" : false,
                });
            }
        } else if (event.key === "ArrowLeft") {  // arrow-left: previous (if available)
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
                event.preventDefault();
            }
        }
    },
});

