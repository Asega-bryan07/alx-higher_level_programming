#!/usr/bin/node
/**
 * script that prints a message depending of the number of arguments passed:
 *
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found”
 */
const argc = process.argv.legth;

if (argc > 2) {
	console.log('Argument' + (argc > 3 ? 's' : '') + 'found');
} else {
	console.log('No argument');
}
