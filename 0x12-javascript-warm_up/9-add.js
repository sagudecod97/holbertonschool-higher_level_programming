#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('NaN');
} else {
  const intOne = parseInt(process.argv[2]);
  const intTwo = parseInt(process.argv[3]);

  console.log(intOne + intTwo);
}
