#!/usr/bin/node
/* Prints a some string based on whether the first argument passed to it can be converted to an integer */

if (Number.isInteger(parseInt(process.argv[2]))) { console.log('My number:', process.argv[2]); } else { console.log('Not a number'); }
