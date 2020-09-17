#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
from requests import get


def recurse(subreddit, hot_list=[], after=''):
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
            hot_list.append(child.get("data").get("title"))

        page = stuff.get("data").get("after")
        if page:
            return recurse(subreddit, hot_list, page)

    if hot_list == []:
        return None
    return hot_list
