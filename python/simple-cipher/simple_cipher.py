import secrets
from string import ascii_lowercase

#print(ascii_lowercase)

class Cipher(object):
    def __init__(self, key=None):
        if key is None:
            key = "".join([secrets.choice(ascii_lowercase) for x in range(100)])
        self.key = key

    def encode(self, text):
        ## key lengthen, just multiply the key by 100
        if len(text) > len(self.key):
            self.key = self.key * 100
        return "".join(self.rotate(letter[1], self.key[letter[0]]) for letter in enumerate(text))

    def decode(self, text):
        if len(text) > len(self.key):
            self.key = self.key * 100
        return "".join(self.rotate(letter[1], self.key[letter[0]], True) for letter in enumerate(text))

    def rotate(self, original_letter, rotation_letter, reverse=False):
        rt = ascii_lowercase.find(rotation_letter)
        og = ascii_lowercase.find(original_letter)        
        if reverse:
            return ascii_lowercase[(og-rt) % 26]
        return ascii_lowercase[(og+rt) % 26]

