#!/usr/bin/python
import tweepy
import csv #Import csv
from auth import *

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "narendramodi"
# Number of tweets to pull
tweetCount =2

# Calling the user_timeline function with our parameters
tweets= api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in tweets:
   # printing the text stored inside the tweet object
   print(tweet.text)

#if __name__ == '__main__':
    #pass in the username of the account you want to download
    #tweets("narendramodi") #Modify this username

    #declare file paths as follows for three files
data_file = "desktop/fake news/data_file.csv"
COLS=['id','favorite_count', 'retweet_count']
