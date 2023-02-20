#!/usr/bin/node
/* Toggle between 'green' & 'red' class for <header> element when div (id = red_header) is clicked */
const $ = window.$;
$('DIV#toggle_header').on('click', function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
