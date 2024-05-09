#!/usr/bin/python3
"""function that queries reddit api and prints out
the titles of first 10 hot posts listed in subreddit."""

import requests

def top_ten(subreddit):
    """function to query reddit api and prints the titles
    of the first 10 hot posts in subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
            else:
                print("None")
    except Exception:
        print("None")
