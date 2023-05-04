#!/usr/bin/python3
"""
This module gathers data from a REST API to retrieve information
about the TODO list progress for a given employee ID.
"""

import requests
import sys


def gather_data():
    """
    Retrieves the TODO list progress for a given employee ID
    and prints the employee's name and the number of completed tasks.
    """
    # Gets Employee information
    user_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response1 = requests.get(user_url).json()
    EMPLOYEE_NAME = response1.get("name")

    # Get number of tasks done
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response2 = requests.get(todo_url).json()
    TOTAL_NUMBER_OF_TASKS = [
        dict_ for dict_ in response2 if dict_.get("userId") == user_id
    ]
    NUMBER_OF_DONE_TASKS = [
        done for done in TOTAL_NUMBER_OF_TASKS if done.get("completed")
    ]

    print("Employee {} is done with tasks ({}/{})".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS))
    )
    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task.get("title")))

# Make code inexecutable
if __name__ == "__main__":
    gather_data()
