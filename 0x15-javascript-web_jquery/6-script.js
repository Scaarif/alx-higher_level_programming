#!/usr/bin/node
/* Updates the contents of <header> to 'New Header!!!' when div (id = update_header) is clicked */
$('#update_header div').on('click', function () {
  $('header').text('New Header!!!');
});
