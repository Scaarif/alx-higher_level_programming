#!/usr/bin/node
/* Computes the number of tasks completed by user id
 * Takes args, first of which is the API URL to request (GET) using the module 'request'
 * Only prints users with completed task
 */

const request = require('request');
if (process.argv.length > 2) {
  request(process.argv[2], function (error, response, body) {
    if (error) console.log(error);
    const todos = JSON.parse(body);
    const perUser = {};
    for (const todo in Object.keys(todos)) {
      if (todos[todo].completed) {
        if (perUser[todos[todo].userId]) {
          perUser[todos[todo].userId] += 1;
        } else {
          perUser[todos[todo].userId] = 1;
        }
      }
    }
    console.log(perUser);
  });
}
