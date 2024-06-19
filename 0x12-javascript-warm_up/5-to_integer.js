#!/usr/bin/node

const argv = process.argv;
if (Number(argv[2])) { console.log(Number(argv[2]).toFixed()); } else { console.log('Not a number'); }
