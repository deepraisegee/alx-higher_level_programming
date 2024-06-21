#!/usr/bin/node

const { dict } = require('./101-data.js');

const userIdsByOccurrence = {};

for (const [userId, occur] of Object.entries(dict)) {
  if (!userIdsByOccurrence[occur]) {
    userIdsByOccurrence[occur] = [];
  }
  userIdsByOccurrence[occur].push(userId);
}

const finalResult = {};
for (const [occur, userIds] of Object.entries(userIdsByOccurrence)) {
  finalResult[occur.toString()] = userIds;
}

console.log(finalResult);
