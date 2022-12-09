#!/usr/bin/node

exports.convert = function (base) { return num => num.toString(base); };
