import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from TweetsToFile import *

consumer_key = 'MUeFQrXo2pwep7lXiDYjsIiyD'
consumer_secret = 'DUaeIPW93O3W6SPF9eusXWchGotiZw06xi0nSEiBSdzYQVdb5W'
access_token = '3433605718-UoFDJigicnyV8hkH58You42BqstYBqdMkcZiOoC'
access_secret = 'iNwcQDYwJelW3xF5AWZdL05pThYVkRvhvcVTy8p8P2esn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

searches = {}
def add_search(filename,search):
    searches[filename] = search
'''
add_search(
            "earthquakes.txt",
            limited_searchlist("san andreas fault OR\
                               california earthquake OR\
                               earthquake OR\
                               5.7 magnitude",100)
           )
add_search(
            "flooding.txt",
            limited_searchlist("flood flooding OR\
                                warning OR danger OR\
                                damage OR flash OR\
                                storm",200)
           )
'''

for filename, search in searches.items():
    texts_to_file(filename, search)

    txt = open(filename, 'r')
    lines = txt.readlines()
    print filename+":",len(lines)
##    for line in lines:
##        tweet = json.loads(line)
##        print tweet["user"]["name"]+"(@"+tweet["user"]["screen_name"]+"): "+ tweet["text"]
##        print "==========================================="

    txt.close()
