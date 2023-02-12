#!/usr/bin/node
/* Prints the number of movies where the character "Wedge Antilles" is present
 * Takes args, first of which is the URL to request (GET) using the module 'request'
 * Wedge Antilles is character ID 18 - use the ID to filter the results of the API
 */

const request = require('request');
if (process.argv.length > 2) {
  request(process.argv[2], function (error, response, body) {
    if (error) console.log(error);
    // body will contain all films (filter the results by character ID)
    const films = JSON.parse(body).results;
    let count = 0;
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (const film of Object.keys(films)) {
      if (films[film].characters.includes(character, 0)) {
        count += 1;
      }
    }
    console.log(count);
  }
  );
}
