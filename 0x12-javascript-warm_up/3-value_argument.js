#!/usr/bin/node
/**
 * script that prints the first argument passed to it:
 *
 * If no arguments are passed to the script, print “No argument”
 * You must use console.log(...) to print all output
 */
console.log(process.argv[2] ? process.argv[2] : 'No argument');
