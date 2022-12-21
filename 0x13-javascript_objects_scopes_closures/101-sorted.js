#!/usr/bin/node
/* Imports a dict and computes a new dict */
const dict = require('./101-data').dict;
const dict2 = {};
for (const key in dict) {
  if (!dict2[dict[key]]) {
    dict2[dict[key]] = [];
    dict2[dict[key]].push(key);
  } else { dict2[dict[key]].push(key); }
}
console.log(dict2);
