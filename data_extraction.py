import tweepy
import csv
# Creating the authentication object
auth = tweepy.OAuthHandler(BU6vWOlFm0pz1Q9z3PMs3k9NB, YgBrMKlb1S90VBVEIDELqvtzSjHAMMdrmVAFU2SOvy1Gx8O3DO)
# Setting your access token and secret
auth.set_access_token(3170285450-cIsl0DuoWCbdlYhy3CgIZlafz8AdwWouY16Mwli, u4kAyqlIsugwK9sdjAo0anfpW5679G6amsMIzxR6NedJI)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
tweets = api.home_timeline()
