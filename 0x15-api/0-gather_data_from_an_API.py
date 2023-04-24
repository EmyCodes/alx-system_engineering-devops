#!/usr/bin/python3
<<<<<<< HEAD
""" Checks student output for returning info from REST API """

=======
""" Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress """
>>>>>>> parent of 1cdd927... 0-gather_data_from_an_API.py formatted to pycodestyle
import requests
import sys


if __name__ == "__main__":

    # Getting employee details: employee id, employee response, task response
    employeeId = sys.argv[1]
    employeeResponse = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    tasksResponse = requests.get('https://jsonplaceholder.typicode.com/todos?UserId={}'.format(employeeId))

    # parsing JSON response into Python dictionaries
    employeeData = employeeResponse.json()
    tasksData = tasksResponse.json()

<<<<<<< HEAD
    # Getting length of total tasks and total total data
    totalTask = len(tasksData)
=======
    # Getting length of total tasks and total total data 
    totalData = len(tasksData)
>>>>>>> parent of 1cdd927... 0-gather_data_from_an_API.py formatted to pycodestyle
    taskCompleted = [task for task in tasksData if task['completed']]
    numOftaskCompleted = len(taskCompleted)

    # display employed name and TODO list progress
    employeeName = employeeData['name']
    print("Emloyee {} is done with tasks({}/{})".format(employeeName, numOftaskCompleted, totalData))

    # display the Title of tasks completed
    for task in tasksData:
        print("\t {}".format(task['title']))
<<<<<<< HEAD
=======

    
    
>>>>>>> parent of 1cdd927... 0-gather_data_from_an_API.py formatted to pycodestyle
