import requests
from bs4 import BeautifulSoup
import re

class_name = ".TweetTextSize"
container_tags = ["p"]
empty_items = [None, " ", "None"]
twitter_url = "https://twitter.com/"
mentions_pattern = re.compile(r'@AI6ph', re.DOTALL)
name_one = re.compile(r'ai6 portharcourt', re.IGNORECASE | re.DOTALL)
name_two = re.compile(r'ai6 ph', re.IGNORECASE | re.DOTALL)
pic_link = re.compile(r'pic.\S+', re.IGNORECASE | re.DOTALL)
twitter_link = re.compile(r'http://\S+', re.IGNORECASE | re.DOTALL)


def get_elements(twitter_handle):
    """:returns all tweet contents from user"""
    url = twitter_url + twitter_handle
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")

    return soup.select(".TweetTextSize")


def get_user_tweets(twitter_handle):
    """:returns tweets that mention AI6"""
    elements = get_elements(twitter_handle)
    tweets = []
    for post in elements[:20]:
        text = post.getText()
        mention = mentions_pattern.findall(str(text))
        n1 = name_one.findall(str(text))
        n2 = name_two.findall(str(text))
        # check if line contains real text
        if text not in empty_items:
            if mention or n1 or n2 != []:
                tweets.append(text)
    return tweets


def remove_media_url(tweets):
    cleaned_tweets = []
    for tweet in tweets:
        i = twitter_link.sub(r"", tweet)
        t = pic_link.sub(r"", i)
        if t != "":
            cleaned_tweets.append(t)

    return cleaned_tweets

