import tweepy
from Twitter_auths import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


try:
    status = tweepy.API.home_timeline()
    api.update_status('아 왜 안올라가 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
except tweepy.TweepError as Err:
    print(Err.api_code)
    if Err.api_code == 187:
        tweets = '이건 중복 트윗이라 오류난 것임(' + str(Err.api_code) + ')'
        api.update_status(tweets)
    else:
        tweets ='이건 '+ str(Err.api_code) +'번 때문에 오류난것임'
        api.update_status(tweets)