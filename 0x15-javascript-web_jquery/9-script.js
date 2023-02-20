#!/usr/bin/node
/* Fetches from a URL & displays the value of 'hello' from the fetch in a div(id=hello) */
const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
