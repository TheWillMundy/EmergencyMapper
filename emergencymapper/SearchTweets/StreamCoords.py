import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from geopy.geocoders import Nominatim
import re, string

consumer_key = 'MUeFQrXo2pwep7lXiDYjsIiyD'
consumer_secret = 'DUaeIPW93O3W6SPF9eusXWchGotiZw06xi0nSEiBSdzYQVdb5W'
access_token = '3433605718-UoFDJigicnyV8hkH58You42BqstYBqdMkcZiOoC'
access_secret = 'iNwcQDYwJelW3xF5AWZdL05pThYVkRvhvcVTy8p8P2esn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
geolocator = Nominatim()
coordinates = []

class MyListener(StreamListener):
    
    def on_data(self, data):
        tweet_info = json.loads(data)
        if(tweet_info["coordinates"] is None):
            if (tweet_info["user"]["location"] is None):
                print None
            else:
                location = geolocator.geocode(tweet_info["user"]["location"])
                if location is None:
                    print None
                else:
                    if(-21.48<float(location.latitude)<71.23 and -179.855<float(location.longitude)<66.56):
                        coordinates.append([float(location.latitude), float(location.longitude), tweet_info['text']])
        else:
            if(-21.48<tweet_info["coordinates"][0]<71.23 and -179.855<weet_info["coordinates"][1]<66.56):
                coordinates.append( [ tweet_info["coordinates"][0],tweet_info["coordinates"][1], tweet_info['text'] ] )

        print tweet_info['text']
        print coordinates
        return True
 
    def on_error(self, status):
        print status
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['earthquake'])
twitter_stream.filter(track=['hurricane'])
twitter_stream.filter(track=['fire'])
twitter_stream.filter(track=['storm'])

