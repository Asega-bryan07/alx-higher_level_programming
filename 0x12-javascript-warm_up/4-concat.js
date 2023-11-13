#!/usr/bin/node
/**
 * a script that prints two arguments passed to it, in the following format: “ is "
 */
const argv0 = process.argv[2];
const argv1 = process.argv[3];

console.log(`${argv0} is ${argv1}`);
