#Dependencies
import tweepy
import time
import json
import os

# Twitter API Keys
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# api.update_status("Heroku Test")

counter = 0

def deployment(counter): 
    api.update_status("Heroku Test"+ str(counter))
    print("Heroku Test"+ str(counter))

# deployment(counter)

while(True):
    deployment(counter)
    counter += 1
    time.sleep(60)
