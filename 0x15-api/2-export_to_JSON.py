#!/usr/bin/python3
"""Extension of file '0-gather_data_from_an_API.py'.
Exports data in JSON format
"""
import json
import sys
from urllib import request


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    # Make sure that only an integer was passed
    employee_id = int(sys.argv[1])
    employee_id = str(employee_id)
    with request.urlopen(url + 'users?id=' + employee_id) as res:
        response = json.loads(res.read().decode())
        username = response[0].get('username')

    with request.urlopen(url + 'todos?userId=' + employee_id) as res:
        response = json.loads(res.read().decode())

    json_data = {}
    json_data[employee_id] = [{"task": task.get('title'),
                               "completed": task.get('completed'),
                               "username": username} for task in response]
    with open(employee_id + '.json', 'w') as file:
        json.dump(json_data, file)
