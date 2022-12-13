#!/usr/bin/node

const fs = require('fs');
let assert = require('assert'); 
let count = 0;

fs.readWrite(process.argv[2].each(function() {
	if ((this).attr(process.argv[3]) == '18')
		count++;
	console.log(count);
}
