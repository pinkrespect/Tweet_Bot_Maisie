# URL 읽어온다.
from urllib.request import urlopen
# 트위터 API
from twitter import *

try:
    from Twitter_auths import *
except:
    print('Tweet API Key are not exist.')
    exit()

t = Twitter(auth=OAuth(CONSUMER_KEY,
CONSUMER_SECRET,
ACCESS_TOKEN_KEY,
ACCESS_TOKEN_SECRET))

message = '아 ㅡㅡ 이거 참 좋은데 트위터라이브러리가 너무 많아서.. 짜증난다..'

# 트위터 함수를 정의했다.
def tweet(message):
    t.statuses.update(status=message)

try:
    tweet(message)
except:
    tweet(message*2)
