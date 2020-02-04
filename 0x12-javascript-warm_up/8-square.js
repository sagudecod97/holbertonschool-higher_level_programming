#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
}

const argvTwo = parseInt(process.argv[2]);
let string = '';

for (let i = 0; i < argvTwo; i++) {
  for (let j = 0; j < argvTwo; j++) {
    string += 'X';
  }
  console.log(string);
  string = '';
}
