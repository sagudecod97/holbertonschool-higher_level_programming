#!/usr/bin/node
const SquareExtends = require('./5-square');

class Square extends SquareExtends {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let char = c;
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let string = '';
      for (let j = 0; j < this.size; j++) {
        string += char;
      }
      console.log(string);
    }
  }
}

module.exports = Square;
