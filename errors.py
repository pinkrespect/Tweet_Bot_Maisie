"""
errors.

This module catches expectable error  number from tweepy module.
"""


def Error_Codes(integer):
    """
    Function Error_Codes.

    tweepy error module returns for it some integer.
    """

    if integer == 187:
        tweets = ("\nDefeat accepted.\nError Code:",
                  str(integer),
                  ' - 중복 트윗')
    elif integer == 139:
        tweets = ("\nDefeat accepted.\nError Code:",
                  str(integer),
                  ' - Favorite Error')
    elif integer == 186:
        tweets = ("\nDefeat accepted.\nError Code:",
                  str(integer),
                  ' - Too long Tweet.')
    else:
        tweets = ('\nUnexpected Error',
                  '\nERROR CODE: ',
                  str(integer))
    return tweets
