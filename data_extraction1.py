#!/usr/bin/python
import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('BU6vWOlFm0pz1Q9z3PMs3k9NB', 'YgBrMKlb1S90VBVEIDELqvtzSjHAMMdrmVAFU2SOvy1Gx8O3DO')
auth.set_access_token('3170285450-cIsl0DuoWCbdlYhy3CgIZlafz8AdwWouY16Mwli', 'u4kAyqlIsugwK9sdjAo0anfpW5679G6amsMIzxR6NedJI')
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
