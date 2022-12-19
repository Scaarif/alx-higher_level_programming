#!/usr/bin/node

/* Prints "C is fun" x times, where  is the first arguent passed to the script */
const num = parseInt(process.argv[2]);
if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) console.log('C is fun');
} else { console.log('Missing number of occurrences'); }
