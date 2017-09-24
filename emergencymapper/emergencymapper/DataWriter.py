import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from TweetsToFile import *
from OTLIstMaker import *

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
add_search(
            "misc.txt",
            limited_searchlist("the -hurricane -flooding\
                                -earthquake -danger -disaster\
                                -crisis -emergency",200)
           )
add_search(
            "harvey.txt",
            old_tweet_tweetlist("#harvey","2017-08-24","2017-08-29",100)
           )
add_search(
            "irma1.txt",
            old_tweet_tweetlist("#hurricaneirma",
                                "2017-09-09","2017-09-11",100)
           )
add_search(
            "irma2.txt",
            old_tweet_tweetlist("#hurricaneirma",
                                "2017-09-11","2017-09-13",100)
           )
add_search(
            "harveyhelp.txt",
            old_tweet_tweetlist("#houstonhelpneeded","2017-08-28","2017-08-29",100)
           )

add_search(
            "irmasos.txt",
            old_tweet_tweetlist("#irmasos","2017-09-09","2017-09-12",100)
           )
'''
add_search(
            "irmarescue.txt",
            old_tweet_tweetlist("#irmarescue","2017-09-09","2017-09-12",100)
           )


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
