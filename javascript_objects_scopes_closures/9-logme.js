#!/usr/bin/node
let count = 0;
exports.loMe = function (item) { console.log(`${count++}: ${item}`); };
