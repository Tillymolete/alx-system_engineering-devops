#!/usr/bin/python3
""" A script that writes data to a csv file"""

import csv
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
        data_row = []
        is_comp = task.get('completed')
        t_title = task.get('title')
        data_row = [usr_id, username, is_comp, t_title]
        data.append(data_row)
    with open(f"{usr_id}.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
