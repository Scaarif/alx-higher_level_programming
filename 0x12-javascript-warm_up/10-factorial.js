#!/usr/bin/node

/* Computes and prints the factorial of a number (passed as arg) */

// uses a function (define it)
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) { return 1; } else { return (n * factorial(n - 1)); }
}
// invoke the function (call the function)
console.log(factorial(Number.parseInt(process.argv[2])));
