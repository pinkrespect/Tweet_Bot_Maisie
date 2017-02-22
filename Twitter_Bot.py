import tweepy
import sys
import time
import datetime
from tweepy.streaming import StreamListener
from tweepy import Stream
from Twitter_auths import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, ADMIN_SCREEN_NAME
from Twitter_Bot_Errors import *
from Twitter_Bot_Defs import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit =True, wait_on_rate_limit_notify=True)
my_name = '@' + api.me().screen_name.lower()

class Timeline_Listener(StreamListener):
    def on_status(self, status):
        mentions = api.mentions_timeline()
        URLs_dict, follow_yet_dict = Mention(mentions, my_name)

        if URLs_dict is not None:
            for key in URLs_dict:
                print(type(key), key, URLs_dict)
                api.create_favorite(key)
                string = '@' + str(URLs_dict[key][0]) + " " + str(URLs_dict[key][1]) + "\n검색어: " + str(URLs_dict[key][2])
                string += datetime.datetime.fromtimestamp(time.time()).strftime('\n%Y-%m-%d %H:%M:%S')
                try:
                    api.update_status(string, in_reply_to_status_id = key)
                except:
                    api.update_status('@' + URLs_dict[key][0] + " " + URLs_dict[key][1], key)
                    api.update_status('@' + URLs_dict[key][0] + " 검색어: " + URLs_dict[key][2], key)
        if follow_yet_dict is not None:
            string = '@' + str(follow_yet_dict[key][0]) + " Follow accepted."
            string += datetime.datetime.fromtimestamp(time.time()).strftime('\n%Y-%m-%d %H:%M:%S')
        follow_yet_dict.clear()
        URLs_dict.clear()

def Run_Bot():
    print('start process')
    api.update_status("Welcome to Holo-Pearl version 0.00000001.")
    while True:
        try:
            listener = Timeline_Listener()
            stream = tweepy.Stream(auth = auth, listener = listener)
            stream.userstream(_with = 'user', async = False)
        except tweepy.TweepError as e:
            string = datetime.datetime.fromtimestamp(time.time()).strftime('\n%Y-%m-%d %H:%M:%S\n')
            api.update_status(string + Error_Codes(e.api_code))
            print(e)
            pass
        except KeyboardInterrupt:
            api.update_status("Server Shutdown Accepted!")
            exit()
        except KeyError:
            pass
        except:
            print(sys.exc_info())
            pass

Run_Bot()