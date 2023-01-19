#!/usr/bin/python3
"""Script that writes to a csv file, all tasks that are owned by an employee
"""
import csv
import json
import sys
from urllib import request
from urllib import parse


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id = int(sys.argv[1])

    user_url = user_url + '?' + parse.urlencode({'id': employee_id})
    with request.urlopen(user_url) as res:
        response = json.loads(res.read().decode())
        name = response[0].get('name')
        username = response[0].get('username')

    todo_url = todo_url + '?' + parse.urlencode({'userId': employee_id})
    with request.urlopen(todo_url) as res:
        response = json.loads(res.read().decode())

    with open('{}.csv'.format(employee_id), 'w') as f:
        csvfile = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in response:
            csvfile.writerow([employee_id,
                              username,
                              task.get('completed'),
                              task.get('title')])
