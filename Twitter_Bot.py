import tweepy
from Twitter_auths import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.update_status('아 왜 안올라가 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
except tweepy.TweepError as Err:
    print(Err)
    print(type(Err))
## How to use Err to Duplicated Error(no. 187)