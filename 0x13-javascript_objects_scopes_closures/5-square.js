#!/usr/bin/node
/* A class Square that defines a square, initializing instance attribute size and inheriting from Rectangle */
const Rectangle = require('./4-rectangle'); // import Rectangle into module
class Square extends Rectangle {
  // include a constructor (initializer) - is a function
  constructor (size) { // initialize the instance via parent class
    super(size, size);
  }
}
// make the class available outside module
module.exports = Square;
