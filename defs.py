from urllib.parse import quote
"""
change utf-8 to url string.
"""

SITES = {'구글': "http://www.google.com/search?q=",
         '네이버': "http://search.naver.com/search.naver?query="}
SITES_keys = SITES.keys()


def index_extracter(new_text, word):
    """
    index_extracter.

    new_text 라인에서 찾고자 하는 word의 start index와 end index를 반환.
    """
    if word + " " in new_text:
        word_len = len(word)+1
    elif word in new_text:
        word_len = len(word)

    start_index = new_text.find(word)
    end_index = start_index + word_len
    return start_index, end_index


def make_urls()


def categorize(mentions, target_text):

    mentioned = {}
    follow_yet = {}
    for word in mentions:
        lower_text = word.text.lower()
        if target_text in lower_text:
            start_index, end_index = index_extracter(lower_text, target_text)
            lower_text = word.text.replace(word.text[start_index:end_index],
                                           "")

            if (SITES_keys and "팔로") in lower_text:
                mentioned[word.id] = [word.user.screen_name, lower_text]

            elif SITES_keys in lower_text:
                mentioned[word.id] = [word.user.screen_name, lower_text]

            elif "팔로" in lower_text:
                follow_yet[word.id] = [word.user.screen_name, lower_text]

            else:
                return None, None

            urls = make_urls(mentioned)
            return urls, follow_yet
        else:
            return None, None
