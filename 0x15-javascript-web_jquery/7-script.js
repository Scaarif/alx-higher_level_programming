#!/usr/bin/node
/* Fetches the character name from a URL & displays it in a div(id=character) */
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const $ = window.$;
$.get(url, function (data, responseStatus) {
  $('DIV#character').text(data.name);
});
