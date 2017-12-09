// $('.real-btn').on('click', function() {
//
//   $('<span class="plus-one"/>', {
//       style: 'display:none'
//     })
//     .html('+10')
//     .appendTo($('.add-comment'))
//     .fadeIn('1000', function() {
//       var el = $(this);
//       setTimeout(function() {
//         el.remove();
//       }, 2000);
//     });
//
//     var text = $(this).val();
//
//     $.ajax({
//       url: "/new_text",
//       type: "get",
//       data: {text},
//       success: function(response) {
//         $(".tweet--body").html(response);
//       },
//       error: function(xhr) {
//         //Do Something to handle error
//       }
//     });
//
//     var countText = $(this).val();
//
//     $.ajax({
//       url: "/new_count",
//       type: "get",
//       data: {countText},
//       success: function(response) {
//         $(".new-count").html(response);
//       },
//       error: function(xhr) {
//         //Do Something to handle error
//       }
//     });
//
// });
//
// $('.fake-btn').on('click', function() {
//
//   $('<span class="minus-one"/>', {
//       style: 'display:none'
//     })
//     .html('-10')
//     .appendTo($('.add-comment'))
//     .fadeIn('1000', function() {
//       var el = $(this);
//       setTimeout(function() {
//         el.remove();
//       }, 2000);
//     });
//
// });

$('.middle-btn').on('click', function() {

    var text = $(this).val();
    $.ajax({
      url: "/pick_text",
      type: "get",
      data: {text},
      success: function(response) {
        $(".tweet--body").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });

    var countText = $(this).val();
    $.ajax({
      url: "/new_count",
      type: "get",
      data: {countText},
      success: function(response) {
        $(".new-count").html(response);
      }
    });

});

function read_score(countText) {
    $.ajax({
      url: "/read_score",
      type: "get",
      data: {countText},
      success: function(response) {
        $(".text").html(response);
      }
    });
};

function add_score(new_score) {
    $.ajax({
      url: "/add_score",
      type: "get",
      data: {new_score},
      success: function(response) {
        $(".text").html(response);
      }
    });
};

function minus_score(new_score) {
    $.ajax({
      url: "/minus_score",
      type: "get",
      data: {new_score},
      success: function(response) {
        $(".text").html(response);
      }
    });
};

$('.real-btn').on('click', function() {

    var guess = $(this).val();
    $.ajax({
      url: "/correct_guess",
      type: "get",
      data: {guess},
      success: function(response) {

         if(response == "True") {
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

               add_score(guess);
               read_score(guess);


         } else if (response == "False") {
             $('<span class="minus-one"/>', {
                 style: 'display:none'
               })
               .html('-10')
               .appendTo($('.add-comment'))
               .fadeIn('1000', function() {
                 var el = $(this);
                 setTimeout(function() {
                   el.remove();
                 }, 2000);
               });

               minus_score(guess);
               read_score(guess);

         }
      }
    });

});


$('.fake-btn').on('click', function() {

    var guess = $(this).val();
    $.ajax({
      url: "/correct_guess",
      type: "get",
      data: {guess},
      success: function(response) {
         if(response == "True") {

             $('<span class="minus-one"/>', {
                 style: 'display:none'
               })
               .html('-10')
               .appendTo($('.add-comment'))
               .fadeIn('1000', function() {
                 var el = $(this);
                 setTimeout(function() {
                   el.remove();
                 }, 2000);
               });

               minus_score(guess);
               read_score(guess);

         } else if (response == "False") {

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

               add_score(guess);
               read_score(guess);

         }
      }
    });







});
