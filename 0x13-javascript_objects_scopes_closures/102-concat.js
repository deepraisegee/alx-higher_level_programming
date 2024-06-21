#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

// read file
const file1 = fs.readFileSync(argv[2], 'utf8');
const file2 = fs.readFileSync(argv[3], 'utf8');

// write into read
fs.writeFileSync(argv[4], file1 + file2);
