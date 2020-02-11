#!/usr/bin/node
const { dict } = require('./101-data');
const newDictio = {};

for (const key in dict) {
  const value = dict[key];
  newDictio[value] = [];
  for (const keys in dict) {
    if (dict[keys] === value) {
      newDictio[value].push(keys);
    }
  }
}
console.log(newDictio);
