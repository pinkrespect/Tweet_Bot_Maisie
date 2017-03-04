
"""Twitter_Bot."""

import sys
import time
import datetime
import tweepy
from tweepy.streaming import StreamListener
from Twitter_auths import C_KEY, C_SECRET, A_TOKEN_KEY, A_TOKEN_SECRET
from Twitter_Bot_Errors import Error_Codes
from Twitter_Bot_Defs import Mention


if __name__ == "__main__":
    print("loading Twitter_Bot.py")
else:
    raise KeyboardInterrupt


AUTH = tweepy.OAuthHandler(C_KEY, C_SECRET)
AUTH.set_access_token(A_TOKEN_KEY, A_TOKEN_SECRET)

api = tweepy.API(AUTH, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
me = api.me()
my_name = '@'+(me.screen_name).lower()
# screen_name is in the Twitter_Bot_Auth.


class Timeline_Listener(StreamListener):
    """
    tweepy.StreamListener.

    Listen to Timeline stream
    """

    def on_status(self, status):
        """
        on_status, Timeline_Listener.

        status listener.
        tweepy.on_status()
        override on_status()
        """
        mentions = api.mentions_timeline()
        URLs_dict, follow_yet_dict = Mention(mentions, my_name)

        if URLs_dict is not None:
            for key in URLs_dict:
                print(type(key), key, URLs_dict)
                api.create_favorite(key)
                string = ('@',
                          str(URLs_dict[key][0]),
                          " ",
                          str(URLs_dict[key][1]),
                          "\n검색어: ",
                          str(URLs_dict[key][2]))
                string += (datetime.datetime.fromtimestamp(time.time())
                           .strftime('\n%Y-%m-%d %H:%M:%S'))
                try:
                    api.update_status(string, in_reply_to_status_id=key)
                except:
                    # 상관 없음
                    api.update_status('@',
                                      URLs_dict[key][0],
                                      " ",
                                      URLs_dict[key][1], key)
                    api.update_status('@',
                                      URLs_dict[key][0],
                                      " 검색어: ",
                                      URLs_dict[key][2], key)
        """if follow_yet_dict is not None:
            string = '@' + str(follow_yet_dict[key][0]) + " Follow accepted."
            string += (datetime.datetime.fromtimestamp(time.time())
                       .strftime('\n%Y-%m-%d %H:%M:%S'))"""
        follow_yet_dict.clear()
        URLs_dict.clear()


def Run_Bot():
    """
    Run_Bot.

    actually Bot will run here.
    """
    print('start process')
    api.update_status("Welcome to Holo-Pearl version 0.00000001.")
    while True:
        try:
            listener = Timeline_Listener()
            stream = tweepy.Stream(auth=AUTH, listener=listener)
            stream.userstream(_with='user', async=False)
        except tweepy.TweepError as e:
            string = (datetime.datetime.fromtimestamp(time.time())
                      .strftime('\n%Y-%m-%d %H:%M:%S\n'))
            api.update_status(string + Error_Codes(e.api_code))
            print(e)
        except KeyboardInterrupt:
            api.update_status("Server Shutdown Accepted!")
            exit()
        except KeyError:
            pass
        except:
            # 상관 없음
            print(sys.exc_info())


Run_Bot()
