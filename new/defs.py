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
    if target_word + " " in rough_mention:
        target_len = len(target_word)+1
    elif target_word in rough_mention:
        target_len = len(target_word)  # TODO: It's so dirty parsing method.
    # If there is no target_word in rough_mention.
    else:
        return False

    start = rough_mention.find(target_word)
    end = start + target_len

    return start, end  # TODO: Is this it's best?


def mention(mentions, MY_NAME):
    """Mention def.

    Determines whether to send mentions in the received mentions.
    """
    # It uses Dictionary because we can use tweet.id field as the it's key.
    DATA = {}
    FOLLOWS = {}

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
            """
            tender_mention = mention.text.replace(mention.text[start:end], "")
            tender_list = tender_mention.split(" ")
            
            # If tender_mention has Korean word "팔로"
            if extract_index(tender_list, "팔로") is not False:
                
                # If tender_mention include any search engine's name,
                if any(KEY for KEY in tender_list if KEY in SITES_KEYS):
                    # TODO: This part maybe wierd.
                    # DATA dict will be make answer for search term.
                    DATA[mention.id] = [mention.user.screen_name,
                                        tender_mention]
                
                # If there is no search engine's name,
                else:
                    # This can be guessed as a follow request.
                    FOLLOWS[mention.id] = [mention.user.screen_name,
                                           tender_mention]
            # If there is no Korean word "팔로",
            else:
                DATA[mention.id] = [mention.user.screen_name, tender_mention]

        # For mentions without content.
        else:
            return None, None

        # TODO: make_urls part (../Twitter_Bot_Defs.py - line 51)
