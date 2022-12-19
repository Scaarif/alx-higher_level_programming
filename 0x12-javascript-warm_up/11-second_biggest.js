#!/usr/bin/node

/* searches for the biggest integer in the list of args, assuming that all args can be converted to integers */
if (process.argv.length <= 3) {
  console.log(1);
} else {
  const ints = [];
  const len = process.argv.length - 2;
  for (let i = 2; i < process.argv.length; i++) {
    ints.push(process.argv[i]);
  }
  console.log(ints.sort()[len - 2]);
}
