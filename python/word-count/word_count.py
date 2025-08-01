from collections import Counter
import string

ASCII_SET = set(string.ascii_lowercase + string.digits)

def word_count(string):
    # Remove non numbers and letters
    words = "".join([letter if letter in ASCII_SET else " " for letter in string.lower()])

    # Split into list of words
    words = words.split()

    return Counter(words) # Return count