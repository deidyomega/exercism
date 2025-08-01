def abbreviate(words):
    word_lst = words.replace("-", " ").replace("_", "").split()
    return "".join([x[0] for x in word_lst if x != ""]).upper()
