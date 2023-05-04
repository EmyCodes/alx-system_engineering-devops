#!/usr/bin/python3
"""
This module gathers data from a REST API to retrieve information
about the TODO list progress for a given employee ID.
"""

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
    EMPLOYEE_NAME = user_response.get("name")

    # Get number of tasks done
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todo_url).json()
    TOTAL_NUMBER_OF_TASKS = [
        dict_ for dict_ in todos_response if dict_.get("userId") == user_id
    ]
    NUMBER_OF_DONE_TASKS = [
        done for done in TOTAL_NUMBER_OF_TASKS if done.get("completed")
    ]

    print("Employee {} is done with tasks ({}/{})".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS))
    )
    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task.get("title")))
