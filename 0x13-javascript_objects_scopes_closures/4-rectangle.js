#!/usr/bin/node
/* A class Rectangle that defines a rectangle, initializing instance attributes width and height
 * If w or h is equal to 0 or not positive, creates an empty object (i.e. don't initialize attributes)
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { this.width = w; this.height = h; }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width; this.width = this.height; this.height = temp;
  }

  double () {
    this.width *= 2; this.height *= 2;
  }
}
module.exports = Rectangle;
