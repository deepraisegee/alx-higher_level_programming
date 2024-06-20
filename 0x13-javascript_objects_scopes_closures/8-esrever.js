#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (const i of list) {
    newList.unshift(i);
  }
  return newList;
};
