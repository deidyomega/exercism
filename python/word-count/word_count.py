from collections import Counter

def word_count(string):
    # Remove non numbers and letters
    words = "".join([letter if letter.isalnum() else " " for letter in string.lower()])

    # Split into list of words
    words = words.split()

    return Counter(words) # Return count