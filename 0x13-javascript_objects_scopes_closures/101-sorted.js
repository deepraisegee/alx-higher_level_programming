#!/usr/bin/node

const { dict } = require('./101-data.js');
const newObj = {};
Object.values(dict).forEach(x => Object.keys(dict));
