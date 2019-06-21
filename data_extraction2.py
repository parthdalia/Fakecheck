import tweepy
import csv #Import csv
consumer_key = 'BU6vWOlFm0pz1Q9z3PMs3k9NB'
consumer_secret = 'YgBrMKlb1S90VBVEIDELqvtzSjHAMMdrmVAFU2SOvy1Gx8O3DO'
access_token = '3170285450-QSdaPUEM66yZA3eqqGDh4xsVlg2eFvL7PfLNLuZ'
access_token_secret = 'KF2DZ5Hluy9JtGj449EvZNI0Fi0wvjS7STiDncPcwzFEP'

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
