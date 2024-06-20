#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }

  charPrint (c) {
    const l = c === 'undefined' ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += l;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
