#!/usr/bin/node
/* Fetches from a URL & displays the value of 'hello' from the fetch in a div(id=hello) */
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data, responseStatus) {
    $('#hello div').text(data.hello);
  });
});
