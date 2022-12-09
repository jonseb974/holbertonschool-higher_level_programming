#!/usr/bin/node

let x = process.argv[2];
let string = '';
for (let i = 0; i < x; i++) {
	for (let j = 0; j < 1; j++) {
		string += 'C is fun';
	}
	string  += '\n';
}
console.log(string);
