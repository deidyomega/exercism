import string

LOWER = list(string.ascii_lowercase)
UPPER = list(string.ascii_uppercase)

def rotate(value, number):
    value = list(value)
    output = ""
    for letter in value:
        if letter in LOWER:
            output += LOWER[(LOWER.index(letter) + number) % 26]
        elif letter in UPPER:
            output += UPPER[(UPPER.index(letter) + number) % 26]
        else:  #Assume punctuation
            output += letter
    return output