#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me causing the server to respond with a msg containing 'You got me!' in res body
curl -s 0.0.0.0:5000/catch_me
