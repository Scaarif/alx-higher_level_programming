#!/usr/bin/node
module.exports.addMeMaybe = function (x, theFunction) {
  x++;
  theFunction(x);
};
