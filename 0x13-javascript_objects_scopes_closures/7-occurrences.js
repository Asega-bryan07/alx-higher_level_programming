#!/usr/bin/node
/**
 *  a function that returns the number of occurrences in a list:
 *
 *  Prototype: exports.nbOccurences = function (list, searchElement)
 */
exports.nbOccurences = function (list, searchElement) {
	let count = 0;
	for (let i = 0; i < list.length; i++) {
		count = (list[i] === searchElement ? count + 1
			: count);
	}
	return count;
};
