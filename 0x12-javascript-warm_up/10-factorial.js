#!/usr/bin/node
function factorial (num) {
  let result = 0;
  if (num === 0) {
    return (1);
  } else {
    result = factorial(num - 1);
  }
  return result * num;
}

if (process.argv.length <= 2) {
  console.log(1);
} else {
  const argvTwo = process.argv[2];
  const factor = factorial(parseInt(argvTwo));

  console.log(factor);
}
