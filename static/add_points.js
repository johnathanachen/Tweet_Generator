$('.new-tweet-btn').on('click', function() {

  $('<span class="plus-one"/>', {
      style: 'display:none'
    })
    .html('+10')
    .appendTo($('.add-comment'))
    .fadeIn('1000', function() {
      var el = $(this);
      setTimeout(function() {
        el.remove();
      }, 2000);
    });

    var text = $(this).val();

    $.ajax({
      url: "/new_text",
      type: "get",
      data: {text},
      success: function(response) {
        $(".tweet--body").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });

});
