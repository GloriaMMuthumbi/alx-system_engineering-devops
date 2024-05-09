#!/usr/bin/python3
"""recursive function querring reddit api and returns a list
of titles of all hot articles for given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """function that returns a list of titles of all hot posts in
    a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    params = {
            "after": after,
        "count": count,
        "limit": 100
        }
    response = requests.get(url, headers=headers, params=params,
                             allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get('data')
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
