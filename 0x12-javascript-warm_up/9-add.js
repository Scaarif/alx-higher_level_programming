#!/usr/bin/node

/* Prints the addition of 2 integers (passed as args) */

// uses a function (define it)
function add (a, b) {
  console.log(a + b);
}
// invoke the function (call the function)
if (process.argv.length <= 3) { console.log(NaN); } else { add(parseInt(process.argv[2]), parseInt(process.argv[3])); }
