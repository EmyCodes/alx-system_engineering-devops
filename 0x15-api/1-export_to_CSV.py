#!/usr/bin/python3
"""
This module gathers data from a REST API to retrieve information
about the TODO list progress for a given employee ID.
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    """
    Retrieves the TODO list progress for a given employee ID
    and exports the data to a CSV file.
    """
    # Get employee information
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url).json()
    username = user_response.get("username")

    # Get tasks information
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todo_url).json()

    # Filter tasks owned by the employee
    tasks = [
        [user_id, username, task.get("completed"), task.get("title")]
        for task in todos_response
        if task.get("userId") == user_id
    ]

    # Export data to CSV file
    filename = "{}.csv".format(user_id)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ])
        writer.writerows(tasks)
