import tweepy
import logging
import os

# debug code: please do not remove - just comment out
logger = logging.getLogger("tweepy")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="tweepy.log")
logger.addHandler(handler)

# plug your own details in here
consumer_key = 1
consumer_secret = 1
access_token = 1
access_token_secret = 1

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# code start
# open file

ids = [0]

# break urls into user id's
for i in range(len(ids)):
   id = ids(i) 
   api.get_friends(id)
