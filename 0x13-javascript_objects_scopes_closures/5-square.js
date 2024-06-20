#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h) return;
    if (w <= 0 || h <= 0) return;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
