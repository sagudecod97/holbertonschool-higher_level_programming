#!/usr/bin/node
const console = require('console');
let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
