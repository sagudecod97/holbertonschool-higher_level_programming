#!/usr/bin/node
const { list } = require('./100-data');

const newList = [];
list.map((elem, i) => {
  newList.push(elem * i);
});
console.log(list);
console.log(newList);
