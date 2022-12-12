#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], 'utf-8', (err) => { if (err) throw err; });
