def abbreviate(words):
    words = words.replace("-", " ")
    words = words.replace("_", "")
    word_lst = words.split(" ")
    output = ""
    for item in word_lst:
        if item == "":
            continue
        output += item[0]
    return output.upper()


print(abbreviate("Something - I made up from thin air"), "SIMUFTA")