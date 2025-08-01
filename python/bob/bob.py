import string
def hey(text):
    text = text.strip()
    ##### Test for blank:
    if not text:
        return 'Fine. Be that way!'

    ##### Test for SHOUTING
    if text.isupper():
        return "Whoa, chill out!"

    ##### Test if question 
    if text[-1] == "?":
        return "Sure."
    
    ##### Return fallback
    return 'Whatever.'