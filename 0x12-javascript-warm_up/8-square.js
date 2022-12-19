#!/usr/bin/node

/* Prints a square using the character "X". size is the first argument passed */
const num = parseInt(process.argv[2]);
if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) { console.log('X'.repeat(num)); }
} else { console.log('Missing size'); }
