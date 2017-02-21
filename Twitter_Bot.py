import tweepy
from Twitter_auths import *
from Twitter_Bot_Defs import *
from Twitter_Bot_Errors import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
my_name = '@' + api.me().screen_name.lower() # my_name = str
# api.me().screen_name is sometimes doesn't fit who mentioned lower or upper case screen name.

try:
    #mentioned_id, mentioned_user, mentioned_text =
    Mention(api.mentions_timeline(), my_name)
    #if mentioned_id+mentioned_user+mentioned_text != 0:
        # mentioned_user & mentioned_text need to change data type
    #    print('https://www.twitter.com/'+ mentioned_user +'/status/'+ mentioned_id, mentioned_text)
    #else:
    #    raise Unexceptable_Error()
    pass
except tweepy.TweepError as Err:
    api.update_status(Error_Codes(Err.api_code))

except Unexceptable_Error:
    api.update_status(Error_Codes(000) + ADMIN_SCREEN_NAME)