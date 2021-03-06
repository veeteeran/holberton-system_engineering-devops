#!/usr/bin/python3
""" prints the titles of the first 10 hot posts
    listed for a given subreddit
"""
from requests import get


def top_ten(subreddit):
    about = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    hot = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0\
               (Macintosh; Intel Mac OS X 10_15_6)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/85.0.4183.102 Safari/537.37'}
    about_req = get(about, headers=headers)

    if about_req.json().get("kind") == "t5":
        param = {"limit": 10}
        hot_req = get(hot, headers=headers, params=param)
        data = hot_req.json().get("data")
        children = data.get("children")
        for child in children:
            print(child.get("data").get("title"))
    else:
        print("None")
