#!/usr/bin/node
/* Reads and prints te content of a file
 Takes argumnts: the file path, content of file must be utf-8 and if error occurs during reading, print it
*/

const fs = require('fs');
/* process.arv[2] is the first arg after program name (argv[1]) */
if (process.argv.length > 2) {
  fs.readFile(process.argv[2], function (err, data) {
    if (err) {
      return console.log(err);
    }
    console.log(data.toString());
  });
}
