#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], 'C is fun', (err) => { if (err) throw err; });
