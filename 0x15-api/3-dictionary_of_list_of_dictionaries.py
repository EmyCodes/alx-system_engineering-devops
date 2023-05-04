#!/usr/bin/python3
"""
This module gathers data from a REST API to retrieve information
about the TODO list progress for a given employee ID.
"""

import json
import requests
import sys


if __name__ == "__main__":
    """
    Retrieves the TODO list progress for a given employee ID
    and prints the employee's name and the number of completed tasks.
    """
    # Gets Employee information
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url).json()
    username = user_response.get("username")
    print(username)

    # Get number of tasks done
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todo_url).json()

    output = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos_response if task.get("userId") == user_id
        ]
    }

    # print(output)

    with open("{}.json".format(str(user_id)), "w", encoding="utf-8") as file_:
        json.dump(output, file_)
