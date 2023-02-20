#!/usr/bin/node
/* Adds 'red' class to <header> element when div (id = red_header) is clicked */
$('#red_header div').on('click', function () {
  $('header').addClass('red');
});
