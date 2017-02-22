import tweepy
import sys
import time
import datetime
import threading
from tweepy.streaming import StreamListener
from tweepy import Stream
import time
from Twitter_auths import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, ADMIN_SCREEN_NAME
from Twitter_Bot_Errors import *
from Twitter_Bot_Defs import *

'''  스레딩 하고 십다 스레딩 이게 에러가 왜나나 햇더니 
하나 처리중인데 다른새럼이 말걸면 애러나는거같음 에러코드:139인가 129
메ㅐ모리잘못접근 에러남 ㅠㅠ '''

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
                api.create_favorite(key)
                string = '@' + str(URLs_dict[key][0]) + " " + str(URLs_dict[key][1]) + "\n검색어: " + str(URLs_dict[key][2])
                string += datetime.datetime.fromtimestamp(time.time()).strftime('\n%Y-%m-%d %H:%M:%S')
                api.update_status(string, key)
        if follow_yet_dict is not None:
            for key in follow_yet_dict:
                api.create_favorite(key)
                string = '@' + str(follow_yet_dict[key][0]) + " Follow accepted."
                string += datetime.datetime.fromtimestamp(time.time()).strftime('\n%Y-%m-%d %H:%M:%S')
        follow_yet_dict.clear()
        URLs_dict.clear()

def Run_Bot():
    print('start process')
    while True:
        try:
            listener = Timeline_Listener()
            stream = tweepy.Stream(auth = auth, listener = listener)
            stream.userstream(_with = 'user', async = False)
        except tweepy.TweepError as e:
            string = datetime.datetime.fromtimestamp(time.time()).strftime('\n%Y-%m-%d %H:%M:%S\n')
            api.update_status(string + Error_Codes(e.api_code))
            print(e)
            print('time to sleep')
            time.sleep(60)
        except:
            pass

Run_Bot()