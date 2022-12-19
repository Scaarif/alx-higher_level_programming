#!/usr/bin/node
/* Prints a message depending on the number of arguments passed */

if (process.argv.length <= 2) {
  /* Turns out:
   * * argv[0] is node's path & argv[1], the program/script's path
   */
  console.log('No argument');
} else if (process.argv.length === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
