class Clock(object):
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = (hour + (minute // 60)) % 24

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

