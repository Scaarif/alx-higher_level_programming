#!/usr/bin/node
/* Imports an array and computes a new array */
const list = require('./100-data');
console.log(list);
const list2 = list.map((x, index) => x * index);
console.log(list2);
