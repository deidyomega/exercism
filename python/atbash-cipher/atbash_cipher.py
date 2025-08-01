from string import ascii_lowercase as abc

CIHPER_TEXT = dict(zip(list(abc), list(abc)[::-1]))

def cipher(letter):
    if letter in abc:
        return CIHPER_TEXT[letter]
    if letter.isdigit():
        return letter
    return ""

def encode(plain_text):
    ciphered = "".join((cipher(letter) for letter in plain_text.lower()))
    
    return " ".join([ciphered[i:i+5] for i in range(0, len(ciphered), 5)])

def decode(ciphered_text):
    return encode(ciphered_text).replace(" ", "")
