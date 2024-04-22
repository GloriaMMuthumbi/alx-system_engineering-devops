#!/usr/bin/python3
"""Exports list information to JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "userS").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dupm({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
                } for t in requests.get(url + "todos",
                                        params={"userId": u.get("id")}).json()]
                for u in users}, jsonfile)
