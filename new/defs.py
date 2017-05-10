"""
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

