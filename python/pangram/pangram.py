import string

def is_pangram(value):
    letters = set(string.ascii_lowercase)
    value = set(value.lower())
    ## set.intersection(set2) basically asks, how many items are in common.
    ## Since that's all we are trying to do, the answer should be 26 (the number
    ## of letters in the english alphabet)
    return len(value.intersection(letters)) == 26