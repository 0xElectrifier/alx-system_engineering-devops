#!/usr/bin/python3
"""Extension of task #0, exports data in JSON format
Records all tasks from all employees
"""
import json
import sys
from urllib import request
from urllib import parse


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    with request.urlopen(url + 'users') as users:
        users = json.loads(users.read().decode())

    all_data = {}
    for user in users:
        username = user.get('username')
        user_id = str(user.get('id'))
        with request.urlopen(url + 'todos?userId=' + user_id) as todo_res:
            todo_res = json.loads(todo_res.read().decode())
        # Fetch list of a user's tasks
        user_data = [{"username": username,
                      "task": task.get('title'),
                      "completed": task.get('completed')} for task in todo_res]
        all_data[user_id] = user_data

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_data, file)
