#!/usr/bin/python3
""" queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
"""
from requests import get


def count_words(subreddit, word_list=[], after=''):
    """ Calling function """
    headers = {'user-agent': 'Mozilla/5.0\
               (Macintosh; Intel Mac OS X 10_15_6)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/85.0.4183.102 Safari/537.37'}

    hot = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    hot_req = get(hot, headers=headers)
    stuff = hot_req.json()
    if stuff.get("data") and stuff['data'].get('children'):
        children = stuff.get("data").get("children")
        for child in children:
            word_list.append(child.get("data").get("title"))

        page = stuff.get("data").get("after")
        if page:
            return count_words(subreddit, word_list, page)

    if word_list == []:
        return None
    return word_list
