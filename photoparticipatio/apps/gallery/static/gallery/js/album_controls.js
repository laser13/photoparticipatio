/**
 * User: G@mOBEP
 *
 * Company: RealWeb
 * Date: 24.10.12
 * Time: 12:49
 */
(function($){$(function(){
    var AlbumControls = new function()
    {
        var objAlbumControls = this;

        this.init = function()
        {
            var deleteAlbumControls = $('.delete-album-control');
            $.each(deleteAlbumControls, function(i, control)
            {
                control = $(control);

                control.on('click', function()
                {
                    if (control.data('disabled') || !confirm('Удалить альбом?'))
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
        };
        this.init();
    };
});})(jQuery);
