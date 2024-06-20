#!/usr/bin/node

exports.converter = function (base) {
  return function(ten) {
    return ten.toString(base);
  }
}
