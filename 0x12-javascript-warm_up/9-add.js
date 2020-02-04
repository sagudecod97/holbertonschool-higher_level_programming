#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('NaN');
} else {
  let intOne = parseInt(process.argv[2]);
  let intTwo = parseInt(process.argv[3]);

  console.log(intOne + intTwo);
}
