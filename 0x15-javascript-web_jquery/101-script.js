#!/usr/bin/node
/* Adds, removes and clears a <ul> (class=my_list) depending on div(identified by id) clicked */
const $ = window.$;
$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
