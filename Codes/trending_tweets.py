import tweepy
#import json
import csv
from auth import *

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
language='en'

file = open('/home/yash1709/Documents/Fakecheck/Data/TrendingData.csv', 'w+',encoding="utf-8")
csvwriter = csv.writer(file)
header=['User Name','Tweet ID','Tweet']
csvwriter.writerow(header)

trending=api.trends_place(1)
query=trending[0]['trends'][0]['name']

trend_tweets=api.search(q=query,lang=language, count = 100)
for x in trend_tweets:
    name=None
    tweet_id=x.id
    tweet_text=x.text
    data=[name,tweet_id,tweet_text]
    csvwriter.writerow(data)
file.close()
