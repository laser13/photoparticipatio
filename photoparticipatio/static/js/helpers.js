/**
 * Created by G@mOBEP
 *
 * Company: Realweb
 * Date: 30.05.12
 * Time: 11:39
 */
var ObjectHelper = new function()
{
    /**
     * Получение параметра объекта
     *
     * @param obj объект
     * @param param параметр
     * @param def значение по умолчанию
     *
     * @return {*} значение параметра
     */
    this.getParam = function(obj, param, def)
    {
        if (typeof def == 'undefined')
        {
            def = null;
        }

        if (typeof obj != 'object' || typeof obj[param] == 'undefined')
        {
            return def;
        }

        return obj[param];
    };
};

var FormHelper = new function()
{
    /**
     * Блокировка формы
     *
     * @param form форма
     */
    this.disableForm = function(form)
    {
        var elements = form.find(
            'button,' +
                'select,' +
                'textarea,' +
                'input[type="button"],' +
                'input[type="text"],' +
                'input[type="password"],' +
                'input[type="email"],' +
                'input[type="radio"],' +
                'input[type="checkbox"]'
        );

        elements.filter('[disabled="disabled"]').addClass('fhDisabledDef');

        elements.attr('disabled', 'disabled');
    };

    /**
     * Разблокировка формы
     *
     * @param form форма
     */
    this.enableForm = function(form)
    {
        var elements = form.find(
            'button,' +
                'select,' +
                'textarea,' +
                'input[type="button"],' +
                'input[type="text"],' +
                'input[type="password"],' +
                'input[type="email"],' +
                'input[type="radio"],' +
                'input[type="checkbox"]'
        );

        elements.not('.fhDisabledDef').removeAttr('disabled');
        elements.filter('.fhDisabledDef').removeClass('fhDisabledDef');
    };

    /**
     * Вывод ошибок
     *
     * @param msgBox блок отображения сообщений
     * @param errors список ошибок
     */
    this.showErrors = function(msgBox, errors)
    {
        msgBox = $(msgBox);

        if (typeof errors !== 'object' && typeof errors !== 'array')
        {
            errors = [errors];
        }

        var errorsHtml = '';
        if (!msgBox.is('ul'))
        {
            errorsHtml = '<div class="alert alert-error"><button type="button" class="close" data-dismiss="alert">×</button>';
        }
        $.each(errors, function(key, msg)
        {
            errorsHtml += '<div class="error-msg">' + msg + '</div>';
        });
        if (!msgBox.is('ul'))
        {
            errorsHtml += '</div>';
        }

        msgBox.html(errorsHtml).show();
    }
};