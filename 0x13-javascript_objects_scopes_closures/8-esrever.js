#!/usr/bin/node
exports.esrever = function (list) {
  const returnList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    returnList.push(list[i]);
  }

  return returnList;
};
