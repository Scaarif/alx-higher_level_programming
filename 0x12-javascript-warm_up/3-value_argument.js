#!/usr/bin/node
/* Prints the first argument passed to it */

if (process.argv[2]) {
  /* Turns out:
   * * argv[0] is node's path & argv[1], the program/script's path
   */
  console.log(process.argv[2]);
} else { console.log('No argument'); }
