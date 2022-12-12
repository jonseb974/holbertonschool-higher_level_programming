#!/usr/bin/node

const fs = require('fs')
fs.readFile((err, inputD) => {
	if (err) trow err;
	else {
		console.log("Error: ENOENT: no such file or directory, open 'doesntexist'")
	}
})
