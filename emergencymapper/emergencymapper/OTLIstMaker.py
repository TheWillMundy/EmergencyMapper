import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import got

consumer_key = 'MUeFQrXo2pwep7lXiDYjsIiyD'
consumer_secret = 'DUaeIPW93O3W6SPF9eusXWchGotiZw06xi0nSEiBSdzYQVdb5W'
access_token = '3433605718-UoFDJigicnyV8hkH58You42BqstYBqdMkcZiOoC'
access_secret = 'iNwcQDYwJelW3xF5AWZdL05pThYVkRvhvcVTy8p8P2esn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def old_tweet_tweetlist(query,start_date,end_date,limit):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(start_date).setUntil(end_date).setMaxTweets(limit+1)
        tweets = []
        for num in range(limit):
                tweet = got.manager.TweetManager.getTweets(tweetCriteria)[num]
                real_tweet = api.get_status(tweet.id)
                if not real_tweet.retweeted and "RT @" not in real_tweet.text:
                    tweets.append(real_tweet)
                print len(tweets)
        return tweets
