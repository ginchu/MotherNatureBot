import tweepy
import time 
#from keys import *
print("This is my Mother Nature twitter bot")

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
# We are going to be using this api object to 
# basically talk to Twitter and read/write data into Twitter

ht1 = '#nature'
ht2 = '#environment'
ht3 = '#climatechange'

def searchRetweet(n):
    for tweet in tweepy.Cursor(api.search, q=n, result_type='popular', lang='en').items(5):
        try:
            # Add \n escape character to print() to organize tweets
            print('\nHashtag: ' + n)
            print('Tweet by: @' + tweet.user.screen_name)

            # Retweet tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet')

            time.sleep(30)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


while True:
    searchRetweet(ht1)
    time.sleep(10800)
    searchRetweet(ht2)
    time.sleep(10800)
    searchRetweet(ht3)
    time.sleep(10800)