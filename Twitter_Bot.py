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
    mentions = api.mentions_timeline()
    mentioned_data_dict = {}
    for mention in mentions:
        mentioned_data_dict[mention] = Mention(mentions, my_name)
        
    #if mentioned_id+mentioned_user+mentioned_text == 0:
    #    print('https://www.twitter.com/'+ mentioned_user +'/status/'+ mentioned_id, mentioned_text)
    #    raise Unexceptable_Error()

except tweepy.TweepError as Err:
    api.update_status(Error_Codes(Err.api_code))

except Unexceptable_Error:
    api.update_status(Error_Codes(000) + ADMIN_SCREEN_NAME)