""" 여기 있는 함수들은 멘션에 쓰일 메세지를 생성하거나, 멘션을 보낼지 말지에 대한 판단을 합니다."""
from urllib.parse import quote

def Mention(mentions, my_name):
    mentioned_data_dict = {}
    follow_yet_dict = {}
    for mention in mentions:
        new_text = mention.text.lower()
        if (my_name in new_text) or (mention.favorited is False):
            start_index, end_index = My_Name_Index(new_text, my_name)
            new_text = mention.text.replace(mention.text[start_index:end_index], "")

            if (("네이버" or "구글") and ("팔로")) in new_text:
                mentioned_data_dict[mention.id] = [mention.user.screen_name, new_text]

            elif "네이버" or "구글" in new_text:
                mentioned_data_dict[mention.id] = [mention.user.screen_name, new_text]

            elif "팔로" in new_text:
                follow_yet_dict[mention.id] = [mention.user.screen_name, new_text]
# 추후 여기에 else 구문 고민 해 볼것
            URLs_dict = {}
            URLs_dict = Make_URLs(mentioned_data_dict)
            print(URLs_dict)
            return URLs_dict, follow_yet_dict
        else:
            return None, None

def My_Name_Index(new_text, my_name):
    if my_name + " " in new_text:
        My_name_len = len(my_name)+1
    elif my_name in new_text:
        My_name_len = len(my_name)

    start_index = new_text.find(my_name)
    end_index = start_index + My_name_len
    return start_index, end_index


def Make_URLs(mentioned_data_dict):
    URLs_dict = {}
    for number in mentioned_data_dict.keys():
        if "네이버" in mentioned_data_dict[number][1]:
            start_index, end_index = My_Name_Index(mentioned_data_dict[number][1], '네이버')
            search_word = mentioned_data_dict[number][1].replace(mentioned_data_dict[number][1][start_index:end_index], "")
            original_word = search_word##
            search_word = quote(search_word, safe='')
            search_word = search_word.replace("%20", "+")
            search_word = 'http://search.naver.com/search.naver?query=' + search_word
            URLs_dict[number] = [mentioned_data_dict[number][0], search_word, original_word]

        if "구글" in mentioned_data_dict[number][1]:
            start_index, end_index = My_Name_Index(mentioned_data_dict[number][1], '구글')
            search_word = mentioned_data_dict[number][1].replace(mentioned_data_dict[number][1][start_index:end_index], "")
            original_word = search_word##
            search_word = quote(search_word, safe='')
            search_word = search_word.replace("%20", "+")
            search_word = 'http://www.google.com/search?q=' + search_word
            URLs_dict[number] = [mentioned_data_dict[number][0], search_word, original_word]
    return URLs_dict

def Follow(follow_yet_dict):
    follow_dict = {}
    return follow_dict