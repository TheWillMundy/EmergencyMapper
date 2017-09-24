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

def main():

        places = api.geo_search(query = 'USA', granularity = 'country')
        places_id = places[0].id
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#Harvey').setSince("2017-08-01").setUntil("2017-08-30").setMaxTweets(51).setWithin("Galveston")
        coordinates = []
        for num in range(50):
                tweet = got.manager.TweetManager.getTweets(tweetCriteria)[num]
                real_tweet = api.get_status(tweet.id)
                print real_tweet.text
                if real_tweet.place != None:
                        x_val1, y_val1 =  (real_tweet.place.bounding_box.coordinates[0][0][0]+real_tweet.place.bounding_box.coordinates[0][3][0])/2, (real_tweet.place.bounding_box.coordinates[0][0][1]+real_tweet.place.bounding_box.coordinates[0][3][1])/2
                        x_val2, y_val2 =  (real_tweet.place.bounding_box.coordinates[0][1][0]+real_tweet.place.bounding_box.coordinates[0][2][0])/2, (real_tweet.place.bounding_box.coordinates[0][1][1]+real_tweet.place.bounding_box.coordinates[0][2][1])/2
                        x_val, y_val = (x_val1 + x_val2)/2, (y_val1 + y_val2)/2
                        coordinates.append([x_val, y_val])
                else:
                        coordinates.append([])
        print coordinates
        return coordinates
if __name__ == '__main__':
        main()

