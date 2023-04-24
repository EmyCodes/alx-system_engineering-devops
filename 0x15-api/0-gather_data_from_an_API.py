#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress """
import requests
import sys


if __name__ == "__main__":

    # Getting employee details: employee id, employee response, task response
    employeeId = sys.argv[1]
    userUrl = f'https://jsonplaceholder.typicode.com/users/{employeeId}'
    todoUrl = f'https://jsonplaceholder.typicode.com/todos?UserId={employeeId}'
    employeeResponse = requests.get(userUrl)
    tasksResponse = requests.get(todoUrl)
    # parsing JSON response into Python dictionaries
    employeeData = employeeResponse.json()
    tasksData = tasksResponse.json()

    # Getting length of total tasks and total total data 
    totalTask = len(tasksData)
    taskCompleted = [task for task in tasksData if task['completed']]
    completedTask = len(taskCompleted)

    # display employed name and TODO list progress
    name = employeeData['name']
    print(f"Emloyee {name} is done with tasks({completedTask}/{totalTask})")

    # display the Title of tasks completed
    for task in tasksData:
        print("\t {}".format(task['title'])) 
