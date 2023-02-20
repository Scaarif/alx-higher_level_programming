#!/usr/bin/node
/* Adds (appends) an <li> item to the <ul> item of class 'my_list' when div (id = red_header) is clicked */
$('#add_item div').on('click', function () {
  $('.my_list ul').append('<li>Item</li>');
});
