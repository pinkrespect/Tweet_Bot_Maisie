import tweepy
import sys
from tweepy.streaming import StreamListener
from tweepy import Stream
import time
from Twitter_auths import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, ADMIN_SCREEN_NAME
from Twitter_Bot_Errors import *
from Twitter_Bot_Defs import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit =True, wait_on_rate_limit_notify=True)
my_name = '@' + api.me().screen_name.lower()
# my_name = str
# api.me().screen_name is sometimes doesn't fit who mentioned lower or upper case screen name.

class Timeline_Listener(StreamListener):
    def on_status(self, status):
        mentions = api.mentions_timeline()
        URLs_dict, follow_yet_dict = Mention(mentions, my_name)
        if URLs_dict is not None:
            for key in URLs_dict:
                string = '@' + str(URLs_dict[key][0]) + " " + str(URLs_dict[key][1]) + "\n검색어: " + str(URLs_dict[key][2])
                api.update_status(string, key)
                api.create_favorite(key)
        #if follow_yet_dict is not None:
        #    pass

    def on_error(self, status_code):
        api.update_status(Error_Codes(status_code))
        return False

def Run_Bot():
    while True:
        listener = Timeline_Listener()
        stream = tweepy.Stream(auth = auth, listener = listener)
        stream.userstream(_with = 'user', async = False)

Run_Bot()