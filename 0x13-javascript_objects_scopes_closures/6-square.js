#!/usr/bin/node
/* A class Square that defines a square, initializing instance attribute size and inheriting from Rectangle */
const Rectangle = require('./4-rectangle'); // import Rectangle into module
class Square extends Rectangle {
  // include a constructor (initializer) - is a function
  constructor (size) { // initialize the instance via parent class
    super(size, size);
  }

  charPrint (letter = 'X') {
    for (let i = 0; i < this.height; i++) { console.log(letter.repeat(this.width)); }
  }
}
// make the class available outside module
module.exports = Square;
