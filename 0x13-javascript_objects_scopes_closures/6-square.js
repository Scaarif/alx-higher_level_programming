#!/usr/bin/node
/* Extends the class, Square */
const Square = require('./5-square'); // import Rectangle into module

Square.prototype.charPrint = function (letter = 'X') {
  for (let i = 0; i < this.height; i++) { console.log(letter.repeat(this.width)); }
};
// make the class available outside module
module.exports = Square;
