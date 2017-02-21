def Mention(object, string):
    My_name_len = len(string)
    mentions = object
    for mention in mentions:
        new_text = mention.text.lower()
        if str(new_text).find(string) >= 0:
            new_text = mention.text.replace(mention.text[new_text.find(string):new_text.find(string)+My_name_len], "")
            return mention.user.screen_name, new_text