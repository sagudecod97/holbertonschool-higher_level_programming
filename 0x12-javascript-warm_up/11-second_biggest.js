#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newArr = [];
  const array = process.argv.slice(2, process.argv.length);
  const maxNumber = Math.max(...array);
  for (let i = 0; i < array.length; i++) {
    if (parseInt(array[i]) !== maxNumber) {
      newArr.push(array[i]);
    }
  }
  console.log(newArr.sort()[newArr.length - 1]);
}
