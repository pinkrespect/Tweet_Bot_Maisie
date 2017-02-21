class Unexceptable_Error(Exception):
    pass
    

def Error_Codes(integer):
    if integer == 187:
        tweets = '이건 중복 트윗이라 오류난 것임 ERROR CODE (' + str(integer) + ')'
        return tweets
    if integer == 000:
        tweets = '알 수 없는 오류임(000) 서버 관리자에게 문의하새요! @'
        return tweets
    else:
        tweets ='이건 ERROR CODE '+ str(integer) +'번 때문에 오류난것임'
        return tweets