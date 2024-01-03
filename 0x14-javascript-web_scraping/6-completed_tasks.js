#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true}, (error, response, body) => {
	if (error) {
		console.log(error);
		return;
	}

	const taskComplete = {};
	body.forEach((todo) => {
		if (todo.completed) {
			if (!taskComplete[todo.userId]) {
				taskComplete[todo.userId] = 1;
			} else {
				taskComplete[todo.userId] += 1;
			}
		}
	});
	console.log(taskComplete);
});
