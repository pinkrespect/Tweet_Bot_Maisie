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
import defs


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

