from urllib.parse import quote

def return_dict(integer, dict1, string1, string2, string3):
    mentioned_data_array = [string1, string2, string3]
    dict1[integer] = {integer:mentioned_data_array} 
    return dict1

# new_text 양식: (검색 사이트) (검색할 단어)

def Mention(mentions, my_name):
    mentioned_data_dict = {}
    follow_yet_dict = {}
    for mention in mentions:
        new_text = mention.text.lower()
        if (new_text.find(my_name) >= 0) or (mention.favorited == False):
            start_index, end_index = My_Name_Index(new_text, my_name)
            new_text = mention.text.replace(mention.text[start_index:end_index], "")

            if (((new_text.find('네이버') or new_text.find('구글')) >= 0) and (new_text.find("팔로우") or new_text.find("팔로"))>= 0):
                mentioned_data_dict[mention.id] = [mention.user.screen_name, new_text]

            elif (new_text.find('네이버') and new_text.find('구글')) >= 0:
                mentioned_data_dict[mention.id] = [mention.user.screen_name, new_text]

            elif (new_text.find("팔로우") and new_text.find("팔로")) >= 0:
                follow_yet_dict[mention.id] = [mention.user.screen_name, new_text]
# 추후 여기에 else 구문 고민 해 볼것
            URLs_dict = {}
            URLs_dict = Make_URLs(mentioned_data_dict)
            print(URLs_dict)
            return URLs_dict, follow_yet_dict
        else:
            return None, None

def My_Name_Index(new_text, my_name):
    if new_text.find(my_name + " ") <= 0:
        My_name_len = len(my_name)+1
    elif new_text.find(my_name) <= 0:
        My_name_len = len(my_name)

    start_index = new_text.find(my_name)
    end_index = new_text.find(my_name) + My_name_len
    return start_index, end_index
    

def Make_URLs(mentioned_data_dict):
    URLs_dict = {}
    for number in mentioned_data_dict.keys():
        if mentioned_data_dict[number][1].find("네이버") >= 0:
            start_index, end_index = My_Name_Index(mentioned_data_dict[number][1], '네이버')
            search_word = mentioned_data_dict[number][1].replace(mentioned_data_dict[number][1][start_index:end_index], "")
            search_word = quote(search_word, safe='')
            URLs_dict[number][2] = search_word##
            search_word = search_word.replace("%20", "+")
            search_word = 'http://search.naver.com/search.naver?query=' + search_word
            URLs_dict[number] = [ mentioned_data_dict[number][0], search_word ]

        if mentioned_data_dict[number][1].find("구글") >= 0:
            start_index, end_index = My_Name_Index(mentioned_data_dict[number][1], '구글')
            search_word = mentioned_data_dict[number][1].replace(mentioned_data_dict[number][1][start_index:end_index], "")
            search_word = quote(search_word, safe='')
            URLs_dict[number][2] = search_word##
            search_word = search_word.replace("%20", "+")
            search_word = 'http://www.google.com/search?q=' + search_word
            URLs_dict[number] = [ mentioned_data_dict[number][0], search_word,  ]

    return URLs_dict

def Follow(follow_yet_dict):
    follow_dict = {}
    return follow_dict