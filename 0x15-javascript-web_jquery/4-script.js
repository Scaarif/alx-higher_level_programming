#!/usr/bin/node
/* Toggle between 'green' & 'red' class for <header> element when div (id = red_header) is clicked */
$('#toggle_header div').on('click', toggleClass($('header')));
function toggleClass (sender) {
  if ($(sender).hasClass('red')) {
    $(sender).removeClass('red');
    $(sender).addClass('green');
  } else {
    $(sender).removeClass('green');
    $(sender).addClass('red');
  }
}
