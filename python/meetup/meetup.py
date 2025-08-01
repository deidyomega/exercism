from datetime import date, timedelta

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def meetup_day(year, month, weekday, descriptor):
    """ 
    year: int - Requested Year
    month: int - Requested Month
    weekday: string - Requested Weekday

    descriptor: - string
    - type1 (iteration): 1st, 2nd, 3rd, 4th, 5th
    - type2 (last, teenth): last, teenth (grab a date 13..19)
    """

    dt = date(year, month, 1)

    # Type 1
    if descriptor in ["1st", "2nd", "3rd", "4th", "5th"]:
        occurrence = 0
        count = int(descriptor[0])
        dt = date(year, month, 1)
        i = 0
        while i < 33:
            if getweekday(dt) == weekday:
                occurrence += 1
            if count == occurrence:
                if dt.month == month:
                    return dt
                else: # We moved past the month we requested
                    raise ValueError

            dt = add_day(dt)
            i += 1
        raise ValueError

    # Type 2: Last
    if descriptor == "last":
        found_date = date(year, month, 1)
        occurrence = 0
        i = 0
        ## Since we are looking the the last, we can start later on in the month
        dt = date(year, month, 22)
        while i < 33:
            if getweekday(dt) == weekday and dt.month == month:
                found_date = dt
            dt = add_day(dt)
            i += 1
        return found_date

    ## Type 2: teenth
    dates = set([13,14,15,16,17,18,19])
    ## Since we are looking for 13..19, we should start at 13
    dt = date(year, month, 13)
    i = 0
    while i < 33:
        if dt.day in dates and weekday == getweekday(dt):
            return dt
        dt = add_day(dt)
        i += 1


def getweekday(dt):
    return WEEKDAYS[dt.weekday()]

def add_day(dt):
    return dt + timedelta(days=1)