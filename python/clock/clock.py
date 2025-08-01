class Clock(object):
    def __init__(self, hour, minute):
        self.minute = minute
        self.hour = hour
        self.__set_clock()

    def __set_clock(self):
        """ Magic happens here """
        cmin = self.minute
        chour = self.hour

        if cmin > 59:
            add_hours = cmin // 60
            sub_hours = 0
            self.minute = cmin % 60
        elif cmin < 0:
            add_hours = 0
            sub_hours = cmin // 60
            self.minute = cmin % 60
        else:
            sub_hours = 0
            add_hours = 0
            self.minute = cmin

        self.hour = (chour + add_hours + sub_hours) % 24

    @staticmethod
    def __justify(item):
        return str(item).rjust(2, "0")

    def __repr__(self):
        return "{}:{}".format(self.__justify(self.hour), self.__justify(self.minute))

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        self.__set_clock()
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.__set_clock()
        return self

print(str(Clock(10, 3) - 3), "10:00")

