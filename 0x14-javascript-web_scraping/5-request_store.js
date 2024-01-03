#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const file = process.argv[3];
const url = process.argv[2];

request(url, (error, response, body) => {
	if (error) {
		console.log(error);
	} else {
		fs.writeFile(file, body, 'utf-8', (error) => {
			if (error) {
				console.log(error);
			}
		});
	}
});
