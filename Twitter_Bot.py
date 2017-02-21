import tweepy, time
from Twitter_auths import *
from Twitter_Bot_Defs import *
from Twitter_Bot_Errors import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
my_name = '@' + api.me().screen_name.lower() # my_name = str
# api.me().screen_name is sometimes doesn't fit who mentioned lower or upper case screen name.

while(1):
    try:
        mentions = api.mentions_timeline()
        URLs_dict, follow_yet_dict = Mention(mentions, my_name)
        if (URLs_dict is not None) and (follow_yet_dict is not None):
             for key in URLs_dict:
                print('@' + str(URLs_dict[key][0]) + " " + str(URLs_dict[key][1]))
                api.update_status('@' + str(URLs_dict[key][0]) + " " + str(URLs_dict[key][1]) + str(URLs_dict[key][2]), key)
                api.create_favorite(key)

        else:
            print('sleep')
            time.sleep(20)
            print('wakeup')

    except tweepy.TweepError as Err:
        api.update_status(Error_Codes(Err.api_code)) #봇 주것을때 타임스탬프 ㅠ
        pass

    except Unexceptable_Error:
        api.update_status(Error_Codes(000) + ADMIN_SCREEN_NAME)
        pass