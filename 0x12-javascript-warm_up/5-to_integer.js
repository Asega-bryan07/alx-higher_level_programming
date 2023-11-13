#!/usr/bin/node
/**
 * a script that prints My number: <first argument converted in integer> 
 * if the first argument can be converted to an integer:
 *
 * If the argument can’t be converted to an integer, print “Not a number”
 */
console.log(parseInt(process.argv[2])
	? `My number: ${parseInt(process.argv[2])}`
	: 'Not a number');
