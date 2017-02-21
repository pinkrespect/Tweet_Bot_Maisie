def return_dict(integer, dict1, string1, string2, string3):
    mentioned_data_array = [string1, string2, string3]
    dict1[integer] = {integer:mentioned_data_array} 
    return dict1

def Mention(mentions, my_name):
    My_name_len = len(my_name)
    mentioned_data_dict = {}
    for mention in mentions:
        new_text = mention.text.lower()
        if (str(new_text).find(my_name) >= 0) and (mention.favorited == False):
            new_text = mention.text.replace(mention.text[new_text.find(my_name):new_text.find(my_name)+My_name_len], "")
            print(type(mention.id_str), type(mention.user.screen_name), new_text, mention.favorited)
            return [mention.id_str, mention.user.screen_name, new_text, mention.favorited]
        #else:
        #    return 0, 0, 0
        # Unexceptable_Error

    return mentioned_data_dict