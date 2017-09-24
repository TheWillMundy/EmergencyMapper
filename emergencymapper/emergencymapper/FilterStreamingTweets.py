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

api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        tweet_info = json.loads(data)
        print tweet_info["text"]+"\n"
        return True
 
    def on_error(self, status):
        print status
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['starbucks'])
