#!/usr/bin/node
/**
 * a class Square that defines a square and inherits from Square of 5-square.js:
 * You must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints 
 * the rectangle using the character c
 * If c is undefined, use the character X
 */
const PrevSquare = require('./5-square.js');

class Square extends PrevSquare {
	charPrint (c) {
		const myChar = c === undefined ? 'X' : c;
		for (let i = 0; i < this.height; i++) {
			let myVar = '';
			let y = 0;
			while (y < this.width) {
				myVar += myChar;
				y++;
			}
			console.log(myVar);
		}
	}
}
module.exports = Square;
