/**
 * User: G@mOBEP
 *
 * Company: RealWeb
 * Date: 25.10.12
 * Time: 14:07
 */
(function($){$(function(){
    this.PhotoEditForm = new function()
    {
        var objPhotoEditForm = this;

        this.submitForm = function(){
            var form = objPhotoEditForm.form;

            if (form.data('disabled'))
            {
                return false;
            }

            form.ajaxSubmit({
                dataType: 'json',
                iframe: true,
                beforeSubmit: function()
                {
                    form.msgBox.hide();

                    //FormHelper.disableForm(form.data('disabled', true));
                },
                success: function(response)
                {
                    if (response.status == 'error')
                    {
                        //FormHelper.enableForm(form.data('disabled', false));
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

        this.init = function()
        {
            this.form = $('.photo-edit-form').eq(0);
            this.form.msgBox = this.form.find('.msg-box').eq(0);

            // ---------------------------------------------

            this.form.on('submit', this.submitForm);
        };
        this.init();
    };
});})(jQuery);
