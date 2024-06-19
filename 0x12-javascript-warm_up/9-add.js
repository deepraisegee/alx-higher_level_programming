#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const argv = process.argv;
const [a, b] = [Number(argv[2]), Number(argv[3])];

add(a, b);
