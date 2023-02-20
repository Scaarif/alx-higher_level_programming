#!/usr/bin/node
/* Fetches and lists the title for all movies from a URL in a <ul>(id=list_movies) */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function(data, responseStatus) {
 for (const movie in Object.values(data)){
  let title = movie.title
  $('#list_movies ul').append($('<li></li>').text(title));
 });
