#!/usr/bin/node
/* Adds 'red' class to <header> element when div (id = red_header) is clicked */
const $ = window.$;
$('DIV#red_header').on('click', function () {
  $('header').addClass('red');
});
