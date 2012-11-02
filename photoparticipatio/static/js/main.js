$(document).ready(function() {

  // Grid view
  $('.toggle-grid').click(function() {
    $(this).addClass('active').siblings().removeClass('active');
      var url = $(this).data('url');
      $('#id-thumbnails').load(url)
  });

  // 230x160
  $('.toggle-grid-detailed').click(function() {
        $(this).addClass('active').siblings().removeClass('active');
        var url = $(this).data('url');
        $('#id-thumbnails').load(url)
  });

  $('.thumbnails').on('mouseover', '.thumbnail-data', function() {
      $(this).siblings('.thumbnail').addClass('hover');
  });
  $('.thumbnails').on('mouseleave', '.thumbnail-data', function() {
      $(this).siblings('.thumbnail').removeClass('hover');
  });

  $('.get-codes, .likes, .index-thumbs .btn-small').tooltip();

});
