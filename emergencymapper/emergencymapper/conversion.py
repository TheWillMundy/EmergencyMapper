import json

def get_tweet(tweet_string):
    '''
    Converts raw tweet string into dictionary and returns converted tweet
    '''
    tweet_dict = json.loads(tweet_string)
    return tweet_dict

def get_user(user_string):
    '''
    Converts raw user string into dictionary and returns converted user
    '''
    user_dict = json.loads(user_string)
    return user_dict
