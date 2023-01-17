#!/usr/bin/python3
""" Takes 2 arguments (repo & owner name) to solve the challenge: List
    10 commits (from the most recent to oldest) of the repository
    "rails" by the user 'rails'.
    Requirements: must use Github API
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
