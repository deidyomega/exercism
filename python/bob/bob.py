import string
def hey(text):
    text = text.strip()
    ##### Test for blank:
    if not text:
        return 'Fine. Be that way!'

    ##### Test for SHOUTING

    # Strip all non alpha chars out
    shouter = "".join([letter for letter in text if letter.isalpha()])

    # Is there anything left, and are all the values uppercase
    if len(shouter) > 0 and all([letter in string.ascii_uppercase for letter in shouter]):
        return "Whoa, chill out!"

    ##### Test if question 
    if text[-1] == "?":
        return "Sure."
    
    ##### Return fallback
    return 'Whatever.'