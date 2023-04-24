#!/usr/bin/python3

""" Checks student output for returning info from REST API """
import requests
import sys


def getEmployeeDetails():
    # Getting employee details: employee id, employee response, task response
    employeeId = sys.argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?UserId={}'.format(employeeId)
    employeeResponse = requests.get(users_url)
    tasksResponse = requests.get(todos_url)

    # parsing JSON response into Python dictionaries
    employeeData = employeeResponse.json()
    tasksData = tasksResponse.json()
    # Getting length of total tasks and total total data
    totalTask = len(tasksData)
    # Getting length of total tasks and total total data
    totalData = len(tasksData)
    taskCompleted = [task for task in tasksData if task['completed']]
    numOftaskCompleted = len(taskCompleted)

    # display employed name and TODO list progress
    employeeName = employeeData['name']
    print("Emloyee {} is done with tasks({}/{})"
          .format(employeeName, numOftaskCompleted, totalData))

    # display the Title of tasks completed
    for task in tasksData:
        print("\t {}".format(task['title']))
if __name__ == "__main__":
	getEmployeeDetails()
