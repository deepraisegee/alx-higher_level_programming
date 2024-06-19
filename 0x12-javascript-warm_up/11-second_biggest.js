#!/usr/bin/node

const argv = process.argv.map(x => Number(x)).slice(2);

if (argv.length <= 1) { console.log(1); } else { console.log(argv.sort((a, b) => b - a)[1]); }
