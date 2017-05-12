"""maisie.py

Twitter_Bot ver 0.5

"""
import sys
import time
import datetime

import tweepy
from tweepy.streaming import StreamListener

from auth import C_KEY, C_SECRET, A_TOKEN_KEY, A_TOKEN_SECRET
# from errors import Error_codes
from defs import guess_mention


# When It imported as module, It raise Keyboard Interrupt error.
if __name__ == "__main__":
    print(" * LOADING Holo Pearl bot * ")
else:
    raise KeyboardInterrupt


"""
Tweepy AUTH handler
"""
AUTH = tweepy.OAuthHandler(C_KEY, C_SECRET)
AUTH.set_access_token(A_TOKEN_KEY, A_TOKEN_SECRET)

API = tweepy.API(AUTH, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


"""
screen_name places in the JSON String.
For make API connection is clear, get MY_NAME and print it.
"""
ME = API.me()
MY_NAME = '@'+(ME.screen_name).lower()

print(" * BOT NAME: " + MY_NAME + " * ")


class Timeline(StreamListener):
    """Timeline class.

    tweepy.StreamLitsener
    Listen Twitter bot's timeline.
    """
    
    def on_status(self, status):
        """on_status in class Timeline.

        status listener.
        override tweepy.on_status()
        """

        mentions = API.mentions_timeline()  # Twitter GET API
        """API.mentions_timeline()

        Returns the 20 most recent mentions, including retweets.

        API.mentions_timeline([since_id ][, max_id ][, count])

        Parameters
            • since_id – Returns only statuses with an ID greater than
            (that is, more recent than) the specified ID.
            • max_id – Returns only statuses with an ID less than
            (that is, older than) or equal to the specified ID.
            • count – Specifies the number of statuses to retrieve.
            Return type list of Status objects

        From Tweepy Doc.
        """

        # def mention() in defs.py
        URLS, FOLLOWS = mention(mentions, MY_NAME)

