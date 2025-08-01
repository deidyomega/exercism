def decode(text):
    output = ""
    tmp_num = ""
    for char in text:
        if char.isnumeric():
            tmp_num += char
        else:
            if tmp_num == "":
                tmp_num = 1
            output += char * int(tmp_num)
            tmp_num = ""

    return output

def encode(text):
    ## The last letter in the for loop is never tested... so we just need a simple endchar
    text += "_"
    count = 0
    curr_char = text[0]
    output = ""
    for letter in text:
        if letter == curr_char:
            count += 1
        else:
            if count > 1:
                output += str(count) + curr_char
            else:
                output += curr_char
            curr_char = letter
            count = 1
    return output