class Luhn(object):
    failed = False
    def __init__(self, card_num):
        if card_num[0] == " ":
            # Special case: if first digit is space, card is invalid
            self.failed = True
        elif card_num == "0":
            # Special case: if card == "0", card is invalid
            self.failed = True
        else:
            self.digits = []
            for digit in card_num:
                if digit.isnumeric():
                    self.digits.append(int(digit))
                elif digit == " ":
                    pass
                else:
                    # if card contains non digit, non spaces, card is invalid
                    self.failed = True
        

    def valid(self):
        ## if failed in parsing
        if self.failed:
            return False

        ## simple copy, to insure each test is valid
        digits = [*self.digits]

        ## actually test card:
        x = len(digits)-2
        while x >= 0:
            digits[x] = digits[x] * 2
            if digits[x] > 9:
                digits[x] -= 9
            x -= 2

        return sum(digits) % 10 == 0

