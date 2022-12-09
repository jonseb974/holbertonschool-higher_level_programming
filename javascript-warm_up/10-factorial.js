#!/usr/bin/node

function factorial(num) {
	if (num > 0) {
		return factorial(num - 1) * num
	} else { 
		return 1;
	}
}
console.log(factorial(process.argv[2]));
