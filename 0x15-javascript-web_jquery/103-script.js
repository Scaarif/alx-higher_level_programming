#!/usr/bin/node
/* Fetches from a URL & displays the value of 'hello' from the fetch in a div(id=hello) depending on language */
const $ = window.$;
let url = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.keyCode === 13) { $('INPUT#btn_translate').click(); }
  });
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    url = url + lang
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
