import tweepy
#import json
import csv

consumer_key = 'BU6vWOlFm0pz1Q9z3PMs3k9NB'
consumer_secret = 'YgBrMKlb1S90VBVEIDELqvtzSjHAMMdrmVAFU2SOvy1Gx8O3DO'
access_token = '3170285450-QSdaPUEM66yZA3eqqGDh4xsVlg2eFvL7PfLNLuZ'
access_token_secret = 'KF2DZ5Hluy9JtGj449EvZNI0Fi0wvjS7STiDncPcwzFEP'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
language='en'

file = open('/home/yash1709/Documents/Fakecheck/TrendingData.csv', 'w+',encoding="utf-8")
csvwriter = csv.writer(file)
header=['User Name','Tweet ID','Tweet']
csvwriter.writerow(header)

trending=api.trends_place(1)
query=trending[0]['trends'][0]['name']

trend_tweets=api.search(q=query,lang=language,count=5)
for x in trend_tweets:
    name=None
    tweet_id=x.id
    tweet_text=x.text
    data=[name,tweet_id,tweet_text]
    csvwriter.writerow(data)
file.close()
