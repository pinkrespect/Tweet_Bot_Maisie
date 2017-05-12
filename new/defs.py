"""defs.py

Definitions in here will do following functions:

    1. Determines whether to send mentions in the received text.
    2. Parsing user's text two parts.
    3. Create messages for mention.
    4. Accept follow request.
    5. String to URL
"""
from urllib.parse import quote

SITES = {'구글': "https://www.google.com/search?q=",
         '네이버': "https://www.naver.com/search.naver?query="}
SITES_KEYS = list(SITES.keys())


if __name__ == "__main__":
    raise KeyboardInterrupt
else:
    print(" ** MAKE dictionary of SITES "
          + SITES_KEYS[0]
          + " "
          + SITES_KEYS[1]
          + " ** ")


def extract_index(rough_mention, target_word):
    """extract_index.

    Extract word or words in new_text string.
    It returns where the word start index and end index.
    """
    if target_word in rough_mention:
        if target_word + " " in rough_mention:
            target_len = len(target_word)+1
        else:
            target_len = len(target_word)
        start = rough_mention.find(target_word)
        end = start + target_len

        # TODO: It's so dirty parsing method.

        return start, end  # TODO: Is this it's best?
    # If there is no target_word in rough_mention.
    else:
        return False, False


def url_parse(data):
    """url_parse def.

    Find right search engine from word in data dictionary,
    and make right string for tweepy def. status_update().
    """
    urls = {}
    """
    We make mention string to send user include URL in this function,
    and store in urls dictionary.
    """
    for tweet_id in data.keys():
        for sites_key in SITES_KEYS:
            start, end = extract_index(data[tweet_id][1], sites_key)
            if (start and end) is True:





def guess_mention(mentions, MY_NAME):
    """guess_mention def.

    Determines whether to send mentions in the received mentions.
    """
    # It uses Dictionary because we can use tweet.id field as the it's key.
    data = {}
    follows = {}

    for mention in mentions:
        """
        Mentions will changes lower case because this part only extract
        and remove @name in mention.
        The original mention content will retained.
        """
        lower_mention = mention.text.lower()

        if MY_NAME in lower_mention:
            start, end = extract_index(lower_mention, MY_NAME)
            """
            tender_mention is a string that has been changed to lowercase
            and @name has been removed.
            tender_list is a list that has been splited by whitespace
            from tender_mention string.
            """
            tender_mention = mention.text.replace(mention.text[start:end], "")
            tender_list = tender_mention.split(" ")

            # If tender_mention has Korean word "팔로"
            if extract_index(tender_list, "팔로") is not False:

                # If tender_mention include any search engine's name,
                if any(KEY for KEY in tender_list if KEY in SITES_KEYS):
                    # TODO: This part maybe wierd in some situation.
                    # DATA dict will be make answer for search term.
                    data[mention.id] = [mention.user.screen_name,
                                        tender_mention]

                # If there is no search engine's name,
                else:
                    # This can be guessed as a follow request.
                    follows[mention.id] = [mention.user.screen_name,
                                           tender_mention]
            # If there is no Korean word "팔로",
            else:
                data[mention.id] = [mention.user.screen_name, tender_mention]

        # For mentions without content.
        else:
            return None, None

        # TODO: make_urls part (../Twitter_Bot_Defs.py - line 51)
