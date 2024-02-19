#!/usr/bin/python3
""" A script that writes data to a json file"""

import json
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
    username = result_1.get('username')

    # find the url that links to the todos page of a given userId
    todos_url = "{}/todos?userId={}".format(base_url, usr_id)
    response_2 = requests.get(todos_url)

    # 'result_2' will be a list of tasks(task dictionaries)
    result_2 = response_2.json()
    # 'data' will be the data to be writen to the csv file
    data = []
    for task in result_2:
        # Single row of data in the csv file
        task_dic = {}
        task_dic['task'] = task.get('title')
        task_dic['completed'] = task.get('completed')
        task_dic['username'] = username
        data.append(task_dic)
    data_dic = {}
    data_dic[usr_id] = data
    with open(f"{usr_id}.json", "w") as jsonfile:
        json.dump(data_dic, jsonfile)
