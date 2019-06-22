import tweepy
import csv #Import csv
from auth import *

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# The search term you want to find
query = "india "
# Language code (follows ISO 639-1 standards)(English-en, Hindi-hi)
language = "en"

# Calling the user_timeline function with our parameters
tweets = api.search(q=query, lang=language)

print(tweets)
