#!/usr/bin/python3
"""
A module containing a function that queries the Reddit API
and prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """ function that prints the 10 hot posts"""

    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']['children']
        for i in range(10):
            print(hot_posts[i]['data']['title'])
    else:
        print(None)
