#!/usr/bin/python3
"""Using REST API, returns information about his/her TODO
list progress"""
import requests
import sys


if __name__ == "__main":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userOD": sys.argv[1]}).json()

    completed = [tget("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
