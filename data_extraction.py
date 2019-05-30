import tweepy
import csv
# Creating the authentication object
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
# Setting your access token and secret
auth.set_access_token('access_token', 'access_token_secret')
# Creating the API object while passing in auth information
api = tweepy.API(auth)
# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
tweets = api.home_timeline()
