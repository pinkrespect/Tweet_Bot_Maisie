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
        if (new_text.find(my_name) >= 0) and (mention.favorited == False):
            start_index, end_index = My_Name_Index(new_text, my_name)
            new_text = mention.text.replace(mention.text[start_index:end_index], "")
            if (((new_text.find('네이버') or new_text.find('구글')) >= 0) and (new_text.find("팔로우") or new_text.find("팔로"))>= 0):
                mentioned_data_dict[mention.id] = [mention.user.screen_name, new_text]
                # 정리된 text, user.Screen_name을 id를 키로 해서 dict에 추가

            elif (new_text.find('네이버') and new_text.find('구글')) >= 0:
                mentioned_data_dict[mention.id] = [mention.user.screen_name, new_text]
                # 정리된 text, user.Screen_name을 id를 키로 해서 dict에 추가

            elif (new_text.find("팔로우") and new_text.find("팔로")) >= 0:
                follow_yet_dict[mention.id] = [mention.user.screen_name, new_text]
                # 정리된 text, user.Screen_name을 id를 키로 해서 follow 대기열 dict에 추가
# 추후 여기에 else 구문 고민 해 볼것
    return Make_URLs(mentioned_data_dict), follow_yet_dict


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
    for number in mentioned_data_dict:
        if mentioned_data_dict[number][1].find("네이버") >= 0: #Naver Search API
            start_index, end_index = My_Name_Index(mentioned_data_dict[number][1], '네이버')
            search_word = mentioned_data_dict[number][1].replace(mentioned_data_dict[number][1][start_index:end_index], "")
            URLs_dict[number] = 'https://search.naver.com/search.naver?where=nexearch&query=+' + search_word + '&sm=top_hty&fbm=1&ie=utf8'
        if mentioned_data_dict[number][1].find("구글") >= 0: #Google Search API
            start_index, end_index = My_Name_Index(mentioned_data_dict[number][1], '구글')
            search_word = mentioned_data_dict[number][1].replace(mentioned_data_dict[number][1][start_index:end_index], "")
            URLs_dict[number] = 'https://www.google.co.kr/webhp?hl=ko&sa=X&ved=0ahUKEwjrn_3Kq6HSAhURObwKHd-qCckQPAgD#hl=ko&q=' + search_word
    return URLs_dict

def Follow(follow_yet_dict):
    follow_dict = {}
    return follow_dict