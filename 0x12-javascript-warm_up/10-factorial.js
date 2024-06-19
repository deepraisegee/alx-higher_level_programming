#!/usr/bin/node

function factorial (num) {
  if (num === 'NaN' || num === 1) { return 1; }

  return num * factorial(num - 1);
}

console.log(factorial(Number(process.argv[2]).toFixed()));
