#!/usr/bin/node
/* Imports an array and computes a new array */
const list = require('./100-data').list;
console.log(list);
/* Note: map  craetes & returns a list (i.e. array) */
console.log(list.map((x, index) => x * index));
