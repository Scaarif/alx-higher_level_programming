#!/usr/bin/node
/* A class Rectangle that defines a rectangle, initializing instance attributes width and height */
class Rectangle {
  // include a constructor (initializer) - is a function
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
// make the class available outside module
module.exports = Rectangle;
