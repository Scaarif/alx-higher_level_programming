#!/usr/bin/node
/* module.exports.<name> - exports a named function:
 * i.e. makes it available outside the module (scope)
 * module.exports.<name> === exports.<name>
 */
module.exports.add = function (a, b) {
  return (a + b);
};
