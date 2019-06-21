import tweepy
import csv

consumer_key = 'BU6vWOlFm0pz1Q9z3PMs3k9NB'
consumer_secret = 'YgBrMKlb1S90VBVEIDELqvtzSjHAMMdrmVAFU2SOvy1Gx8O3DO'
access_token = '3170285450-QSdaPUEM66yZA3eqqGDh4xsVlg2eFvL7PfLNLuZ'
access_token_secret = 'KF2DZ5Hluy9JtGj449EvZNI0Fi0wvjS7STiDncPcwzFEP'

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
tweets = api.home_timeline()

print(tweets)
