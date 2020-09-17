#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
from requests import get


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0\
               (Macintosh; Intel Mac OS X 10_15_6)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/85.0.4183.102 Safari/537.37'}
    req = get(url, headers=headers)
    if req.json().get("kind") == "t5":
        data = req.json().get("data")
        return data.get("subscribers")

    return 0
