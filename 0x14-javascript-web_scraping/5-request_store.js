#!/usr/bin/node
/* Gets the contents of a webpage and stores it in a file
 * Takes args, first of which is the URL to request (GET) using the module 'request'
 * and the second, the file path to store the body of the response
 */

const fs = require('fs');
const request = require('request');
if (process.argv.length > 3) {
  request(process.argv[2], function (error, response, body) {
    if (error) console.log(error);
    // write into file, the response body
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) console.log('fs error: ', err);
    });
  });
}
