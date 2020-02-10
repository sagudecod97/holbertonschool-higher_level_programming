#!/usr/bin/node
const SquareExtends = require('./5-square');

class Square extends SquareExtends {
  charPrint (c) {
    let char = c;
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string += char;
      }
      console.log(string);
    }
  }
}

module.exports = Square;
