#!/usr/bin/node
/* Prints the title of a Star Wars movie where the episode number matches the given integer
 * Takes args, first of which is the integer (ID) of movie to request (GET) using the module 'request' */

const request = require('request');
if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${parseInt(process.argv[2], 10)}`, function (error, response, body) {
    if (error) console.log(error);
    console.log(JSON.parse(body).title);
  }
  );
}
