#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  const cur = number + 1;
  theFunction(cur);
}

module.exports = { addMeMaybe };
