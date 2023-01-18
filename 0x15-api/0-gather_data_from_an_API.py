#!/usr/bin/python3
"""Fetching data from 'JSONPlaceHolder' API using an employee's ID,
returns information about that employee's TODO list progress
"""
import json
from sys import argv
from urllib import parse
from urllib import request


if __name__ == '__main__':
    employee_id = int(argv[1])
    # Fetch employee name first
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    # Encode query string
    query_str = parse.urlencode({'id': employee_id})
    # Format url + query string
    user_url = user_url + '?' + query_str
    with request.urlopen(user_url) as user_res:
        response = user_res.read().decode()
        # Deserialize str object into it json format
        response = json.loads(response)
        name = response[0].get('name')

    # Fetch tasks data
    # Encode query string
    query_str = parse.urlencode({'userId': employee_id})
    # Format url + query string
    todo_url = todo_url + '?' + query_str
    with request.urlopen(todo_url) as todo_res:
        response = todo_res.read().decode()
        response = json.loads(response)

    total_task = len(response)
    # Check number of tasks completed
    task_done = 0
    for task in response:
        if task.get('completed') is True:
            task_done += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          task_done,
                                                          total_task))
    for task in response:
        if task.get('completed') is True:
            print("\t {}\n".format(task.get('title')), end="")
