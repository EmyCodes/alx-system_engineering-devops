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
    and prints the employee's name and the number of completed tasks.
    """
    # Gets Employee information
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url).json()
    username = user_response.get("username")
    # print(username)

    # Get number of tasks done
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todo_url).json()

    output = [

            [
                user_id,
                username,
                task.get("completed"),
                task.get("title"),
            ]
            for task in todos_response
        ]
    

    # print(output)

    
    with open("{}.csv".format(str(user_id)), "w", encoding="utf-8") as file_:
        writer = csv.writer(file_, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(output)
