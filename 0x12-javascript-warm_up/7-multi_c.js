#!/usr/bin/node

const argv = process.argv;

try {
  const count = Number(argv[2]).toFixed();

  if (count === 'NaN') {
    throw new Error();
  }

  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} catch (e) {
  console.log('Missing number of occurrences');
}
