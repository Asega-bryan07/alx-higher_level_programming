#!/usr/bin/node
/**
 * script that prints x times “C is fun”
 *
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print 
 * “Missing number of occurrences”
 * You are not allowed to use var
 * You can use only two console.log
 * You must use a loop (while, for, etc.)
 */
const x = process.argv[2];

if (parseInt !== x) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < x; i++) {
		console.log('C is fun');
	}
}
