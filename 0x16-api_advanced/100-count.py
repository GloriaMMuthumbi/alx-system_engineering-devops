#!/usr/bin/python3
"""script that contains count_words function"""

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """
    Prints the count of given words found in the hot posts of a subreddit

    Args:
        subreddit (str): subreddit to be searched
        word_list (list): list of word to search
        found_list (obj): key/value pairs of count/word
        after (str): parameter for next page of api results
    """
    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
