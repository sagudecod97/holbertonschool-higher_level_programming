#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argv = process.argv;
  const array = argv.slice(2, argv.length);
  const arraySort = array.sort();
  arraySort.pop();
  const lengthSort = arraySort.length;
  console.log(arraySort[lengthSort - 1]);
}
