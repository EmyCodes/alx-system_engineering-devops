#!/usr/bin/python3
"""
This module gathers data from a REST API to retrieve information
about the TODO list progress for all employees.
"""

import json
import requests


if __name__ == "__main__":
    """
    Retrieves the TODO list progress for all employees
    and stores the information in a dictionary of lists of dictionaries.
    """
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url).json()

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todo_url).json()

    output = {}
    for user in user_response:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos_response if task.get("userId") == user_id
        ]
        output[user_id] = tasks

    with open("todo_all_employees.json", "w", encoding="utf-8") as file_:
        json.dump(output, file_)
