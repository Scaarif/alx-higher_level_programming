#!/usr/bin/node
/* A class Rectangle that defines a rectangle, initializing instance attributes width and height
 * If w or h is equal to 0 or not positive, creates an empty object (i.e. don't initialize attributes)
 */
class Rectangle {
  // include a constructor (initializer) - is a function
  constructor (w, h) {
    // Only initialize attributes if w and h > 0
    if (w > 0 && h > 0) { this.width = w; this.height = h; }
  }
}
// make the class available outside module
module.exports = Rectangle;
