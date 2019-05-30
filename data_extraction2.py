import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('BU6vWOlFm0pz1Q9z3PMs3k9NB', 'YgBrMKlb1S90VBVEIDELqvtzSjHAMMdrmVAFU2SOvy1Gx8O3DO')
auth.set_access_token('3170285450-cIsl0DuoWCbdlYhy3CgIZlafz8AdwWouY16Mwli', 'u4kAyqlIsugwK9sdjAo0anfpW5679G6amsMIzxR6NedJI')
api = tweepy.API(auth)

# The search term you want to find
query = " "
# Language code (follows ISO 639-1 standards)(English-en, Hindi-hi)
language = "en"

# Calling the user_timeline function with our parameters
tweets = api.search(q=query, lang=language)
