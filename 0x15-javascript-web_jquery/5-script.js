#!/usr/bin/node
/* Adds (appends) an <li> item to the <ul> item of class 'my_list' when div (id = red_header) is clicked */
const $ = window.$;
$('DIV#add_item').on('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
