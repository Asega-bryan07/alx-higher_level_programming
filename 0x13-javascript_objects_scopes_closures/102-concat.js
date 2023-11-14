#!/usr/bin/node
/**
 * a script that concats 2 files.
 *
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */
const files = require('files');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (files.existsSync(fileA) && files.statSync((fileA).isFile &&
	files.existsSync(fileB) && files.statSync((fileB).isFile &&
		fileC !== undefined) {
		const fileAContent = files.readFileSync(fileA);
		const fileBContent = files.readFileSync(fileB);
		const stream = createWriteStream(fileC);

		stream.write(fileAContent);
		stream.write(fileBContent);
		stream.end();
	}

