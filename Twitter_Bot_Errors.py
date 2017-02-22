import time
import datetime

def Error_Codes(integer):
    if integer == 187:
        tweets = "\nDefeat accepted.\nError Code:" + str(integer) + '- 중복 트윗'
    else:
        tweets = '\nUnexpected Error' + 'ERROR CODE: ' + str(integer)
    return tweets