#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing number of occurences');
} else {
	for (let j = 0; j < size; j++) {
		let row = '';
		for (let i = 0; i < size; i++) {
			row += 'X';
			//console.log(row);
		}
		console.log(row);
	}
}
