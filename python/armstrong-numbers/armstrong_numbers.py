def is_armstrong_number(number):
    number_lst = [int(x) for x in list(str(number))]
    power = len(number_lst)
    return sum(((x ** power) for x in number_lst)) == number
