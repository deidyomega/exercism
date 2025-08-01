import collections
import string

ASCII_SET = set(string.ascii_lowercase + string.digits)

def word_count(string):
    # Setup Counter
    counter = collections.Counter()

    # Handle Control Chars, and lower everything
    string = string.replace("\n", " ").replace("\t", " ").lower()

    # Remove non numbers and letters
    words = "".join([letter if letter in ASCII_SET else " " for letter in string])

    # Split into list of words
    words = words.split()

    for word in words:
        counter[word] += 1

    return dict(counter)