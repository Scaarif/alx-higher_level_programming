#!/usr/bin/node
/* Prints all the characters of a star wars movie
 * Takes args, first of which is the movie ID to request (GET) using the module 'request'
 * Displays oe character name per line & uses the Star Wars API
 */

const request = require('request');
if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${parseInt(process.argv[2], 10)}`, function (error, response, body) {
    if (error) console.log(error);
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) console.log(error);
        console.log(JSON.parse(body).name);
      });
    }
  });
}
