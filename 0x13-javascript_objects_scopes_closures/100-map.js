#!/usr/bin/node
/* Imports an array and computes a new array */
const list = require('./100-data');
console.log(list);
console.log(Array.prototype.map.call(list, (x, index) => x * index));
