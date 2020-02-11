#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const arr = [];

const readA = fs.readFileSync(`./${process.argv[2]}`, (err) => {
  if (err) {
    throw err;
  }
});
arr.push(readA);
const readB = fs.readFileSync(`./${process.argv[3]}`, (err) => {
  if (err) {
    throw err;
  }
});
arr.push(readB);
arr.forEach((read) => {
  fs.appendFileSync(`./${process.argv[4]}`, read, (err) => {
    if (err) {
      throw err;
    }
  });
});
