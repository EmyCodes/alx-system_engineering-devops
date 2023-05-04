#!/usr/bin/python3
import requests
import sys
"""
A Python script that, using this REST API,
for a given employee ID, return information about his/her TODO list progress.
"""

if __name__ == "__main__":
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
    for tasks in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(tasks.get("title")))
