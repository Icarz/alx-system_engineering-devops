#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list of titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles
    of all hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list): A list to store the titles of hot articles.
    after (str): A pagination token to fetch the next set of results.

    Returns:
    titles list of all hot articles.Returns None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alx-api_advanced/1.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                hot_list.append(post.get("data", {}).get("title"))
            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
