import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

consumer_key = 'MUeFQrXo2pwep7lXiDYjsIiyD'
consumer_secret = 'DUaeIPW93O3W6SPF9eusXWchGotiZw06xi0nSEiBSdzYQVdb5W'
access_token = '3433605718-UoFDJigicnyV8hkH58You42BqstYBqdMkcZiOoC'
access_secret = 'iNwcQDYwJelW3xF5AWZdL05pThYVkRvhvcVTy8p8P2esn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

##for status in tweepy.Cursor(api.user_timeline,screen_name = "dril").items(10):
##    tweet = status._json
##    print tweet["text"]+"\n"

##counter = 0
##for result in tweepy.Cursor(api.search,q = "hurricane harvey").items():
####    tweet = result._json
####    print tweet["text"]+"\n"
results = []
for result in tweepy.Cursor(api.search,q = "cats until:2017-09-15").items(10):
    results.append(result)
##print len(results)
##if len(results)>0:
##    print results[-1]._json["created_at"]

cats_txt = open('cats.txt', 'w')
for result in results:
    cats_txt.write(result.__str__)
cats_txt.close()
    
