/**
 * User: G@mOBEP
 *
 * Company: RealWeb
 * Date: 26.10.12
 * Time: 13:51
 */

(function($){$(function(){
    var PhotoControls = new function()
    {
        var objPhotoControls = (this);

        this.init = function()
        {
            // ---------------------------------------
            // удаление фото

            var deletePhotoControls = $('.delete-photo-control');
            $.each(deletePhotoControls, function(i, control)
            {
                control = $(control);

                control.on('click', function()
                {
                    if (control.data('disabled') || !confirm('Удалить фотографию?'))
                    {
                        return false;
                    }

                    control.data('disabled', true);

                    $.post(
                        control.attr('href'),
                        {},
                        function(response){
                            if (response.status == 'success')
                            {
                                window.location = response.url;
                            }
                            else if (response.status == 'error')
                            {
                                alert(response.messages);

                                control.data('disabled', false);
                            }
                        },
                        'json'
                    );

                    return false;
                });
            });

            // ---------------------------------------
            // редактирование фото

            function transform()
            {
                var control = $(this);

                if (control.data('disabled'))
                {
                    return false;
                }

                control.data('disabled', true);

                $.post(
                    control.attr('href'),
                    {},
                    function(response){
                        if (response.status == 'success')
                        {
                            window.location.reload();

                            return;
                        }
                        else if (response.status == 'error')
                        {
                            alert(response.messages);
                        }

                        control.data('disabled', false);
                    },
                    'json'
                );

                return false;
            }

            // поворот на 90 градусов по часовой стрелке
            var rotateForwardControl = $('.rotate-forward-control').eq(0);
            rotateForwardControl.on('click', transform);

            // поворот на 90 градусов против часовой стрелке
            var rotateBackwardControl = $('.rotate-backward-control').eq(0);
            rotateBackwardControl.on('click', transform);

            // отражение по горизонтали
            var flipHorisontalControl = $('.flip-horisontal-control').eq(0);
            flipHorisontalControl.on('click', transform);

            // отражение по вертикали
            var flipVerticalControl = $('.flip-vertical-control').eq(0);
            flipVerticalControl.on('click', transform);
        };
        this.init();
    };
});})(jQuery);
