def steps(number):
    if number < 1:
        raise ValueError("Number must be greater than 0")

    step = 0
    while number != 1:
        if number % 2 == 0: number //= 2
        else: number = (number * 3) + 1
        step += 1
    return step

