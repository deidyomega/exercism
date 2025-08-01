class Phone(object):
    def __init__(self, phone_number):
        phone_number = [n for n in phone_number if n.isdigit()]

        ## Invalid Length
        if len(phone_number) > 11 or len(phone_number) < 10:
            raise ValueError("Bad Number")

        ## Country code included
        if len(phone_number) == 11:
            self.country_code = phone_number[0]
            del phone_number[0]
        else:
            self.country_code = "1"

        self.area_code = "".join(phone_number[0:3])
        self.exchange_code = "".join(phone_number[3:6])
        self.customer_code = "".join(phone_number[6:])
        self.number = self.area_code + \
                      self.exchange_code + \
                      self.customer_code
    
        # Validity checks
        if self.exchange_code[0] in ["0", "1"]:
            raise ValueError("Bad Number")
        if self.area_code[0] in ["0", "1"]:
            raise ValueError("Bad Number")
        if self.country_code != "1":
            raise ValueError("Bad Number")
            
    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.exchange_code, self.customer_code)
