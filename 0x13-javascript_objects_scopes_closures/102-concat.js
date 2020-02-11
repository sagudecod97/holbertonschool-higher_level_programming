#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const arr = [];

const readA = fs.readFileSync(`./${process.argv[2]}`, { encoding: 'UTF-8' }, (err) => {
  console.error(err);
});
arr.push(readA);
const readB = fs.readFileSync(`./${process.argv[3]}`, { encoding: 'UTF-8' }, (err) => {
  console.error(err);
});
arr.push(readB);
arr.forEach((read) => {
  fs.appendFileSync(`./${process.argv[4]}`, read + '\n', { encoding: 'UTF-8' });
});
