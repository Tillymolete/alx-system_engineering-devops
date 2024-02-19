#!/usr/bin/python3
"""A python script that uses REST API to access the todos of a user"""

import requests
import sys

if __name__ == '__main__':
    # The base url for the REST API
    base_url = 'https://jsonplaceholder.typicode.com/'
    # The id given as an argument
    usr_id = sys.argv[1]

    # find the url that links to the users page
    user_url = "{}users/{}".format(base_url, usr_id)
    response_1 = requests.get(user_url)

    # 'result' will be a dictionary containing the detailes of a user with id
    result_1 = response_1.json()

    usr_name = result_1.get('name')

    # find the url that links to the todos page of a given userId
    todos_url = "{}/todos?userId={}".format(base_url, usr_id)
    response_2 = requests.get(todos_url)

    # 'result_2' will be a list of tasks(task dictionaries)
    result_2 = response_2.json()
    # 'completed' will be list of completed tasks
    completed = []
    for task in result_2:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    # Number of completed and total tasks
    c_t = len(completed)
    t_t = len(result_2)

    print("Employee {} is done with tasks({}/{}):".format(usr_name, c_t, t_t))
    for item in completed:
        print("\t {}".format(item))
