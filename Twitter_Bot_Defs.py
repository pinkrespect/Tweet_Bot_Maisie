def return_dict(integer, dict1, string1, string2, string3):
    mentioned_data_array = [string1, string2, string3]
    dict1[integer] = {integer:mentioned_data_array} 
    return dict1

def Mention(object, string):
    My_name_len = len(string)
    mentions = object
    mentioned_data_dict = {}
    for mention in mentions:
        new_text = mention.text.lower()
        if (str(new_text).find(string) >= 0) and (mention.favorited == False):
            new_text = mention.text.replace(mention.text[new_text.find(string):new_text.find(string)+My_name_len], "")
            print(type(mention.id_str), type(mention.user.screen_name), new_text, mention.favorited)
            #return_dict(ee, mentioned_data_dict, mention.id_str, mention.user.screen_name, new_text)
        #else:
        #    return 0, 0, 0
        # Unexceptable_Error

    return mentioned_data_dict