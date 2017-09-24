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

def limited_searchlist(query, limit):
    results = []
    for result in tweepy.Cursor(api.search,q = query).items():
        if not result.retweeted and "RT @" not in result.text:
            results.append(result)
        if len(results)>=limit:
            break
    return results

def unlimited_searchlist(query):
    results = []
    for result in tweepy.Cursor(api.search,q = query).items():
        if not result.retweeted and "RT @" not in result.text:
            results.append(result)
    return results

def tweets_to_file(filename, tweetlist):
    txt = open(filename, 'w')
    txt.truncate()
    for tweet in tweetlist:
        txt.write(json.dumps(tweet._json)+"\n")
    txt.close()

def texts_to_file(filename, tweetlist):
    txt = open(filename, 'w')
    txt.truncate()
    for tweet in tweetlist:
        content = "".join(tweet._json["text"].splitlines())
        txt.write(content.encode("UTF-8")+"\n")
    txt.close()
