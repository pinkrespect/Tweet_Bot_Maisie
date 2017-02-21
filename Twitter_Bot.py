import tweepy
from Twitter_auths import *
from Twitter_Bot_Defs import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
my_name = '@' + api.me().screen_name.lower() # my_name = str
# api.me().screen_name is sometimes doesn't fit who mentioned lower or upper case screen name.

try:
    while(1):
        mentioned_user, mentioned_text = Mention(api.mentions_timeline(), my_name)
        # mentioned_user & mentioned_text need to change data type

except tweepy.TweepError as Err:
    print(Err.api_code)
    if Err.api_code == 187:
        tweets = '이건 중복 트윗이라 오류난 것임(' + str(Err.api_code) + ')'
        api.update_status(tweets)
    else:
        tweets ='이건 '+ str(Err.api_code) +'번 때문에 오류난것임'
        api.update_status(tweets)