#!/usr/bin/node
/* Fetches from a URL & displays the value of 'hello' from the fetch in a div(id=hello) depending on language */
const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('#language_code input').text();
    $.get(url + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
