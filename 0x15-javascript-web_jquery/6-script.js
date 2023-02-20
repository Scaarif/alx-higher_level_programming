#!/usr/bin/node
/* Updates the contents of <header> to 'New Header!!!' when div (id = update_header) is clicked */
const $ = window.$;
$('DIV#update_header').on('click', function () {
  $('header').text('New Header!!!');
});
