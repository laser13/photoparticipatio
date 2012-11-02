/**
 * User: G@mOBEP
 *
 * Company: RealWeb
 * Date: 24.10.12
 * Time: 13:39
 */
(function($){$(function(){
    var AccountsIndexPage = new function()
    {
        var objAccountsIndexPage = this;

        this.init = function()
        {
            this.AccountsForm = new function()
            {
                var objAccountsForm = this;

                /**
                 * Отправка формы
                 */
                this.submitForm = function()
                {
                    var form = objAccountsForm.form;

                    if (form.data('disabled'))
                    {
                        return false;
                    }

                    form.ajaxSubmit({
                        dataType: 'json',
                        beforeSubmit: function()
                        {
                            form.msgBox.hide();

                            FormHelper.disableForm(form.data('disabled', true));
                        },
                        success: function(response)
                        {
                            if (response.status == 'error')
                            {
                                FormHelper.enableForm(form.data('disabled', false));
                                FormHelper.showErrors(form.msgBox, response.messages);
                            }
                            else if (response.status == 'success')
                            {
                                window.location = response.url;
                            }
                        }
                    });

                    return false;
                };

                /**
                 * Инициализация
                 */
                this.init = function()
                {
                    this.form = $('.accounts-form').eq(0);
                    this.form.msgBox = this.form.find('.msg-box-auth').eq(0);

                    // ---------------------------------------------

                    this.form.on('submit', this.submitForm);
                };
            };

            // ---------------------------------------------

            this.AccountsForm.init();
        };
        this.init();
    };
});})(jQuery);