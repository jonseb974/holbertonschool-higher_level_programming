#!/usr/bin/node

const nada = Math.floor(Number(process.argv[2]));
console.log(isNaN(nada) ? 'Not a number' : `My number: ${nada}`);
