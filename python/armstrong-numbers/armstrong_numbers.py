def is_armstrong_number(number):
    power = len(str(number))
    return sum(((int(x) ** power) for x in str(number))) == number
