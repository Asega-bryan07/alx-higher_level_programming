#!/usr/bin/node
/**
 * a script that prints the addition of 2 integers
 *
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 */
const a = process.argv[2];
const b = process.argv[3];

function add(a, b) {
	return (a + b);
}
console.log(add(parseInt(a), parseInt(b)));
