#!/usr/bin/node
/* Updates the text color of the <header> element to red (#ff0000) when div of id 'red_header' is clicked */
const $ = window.$;
$('DIV#red_header').on('click', function () {
  $('header').css('color', '#FF0000');
});
