import math

def rebase(input_base, digits, output_base):
    ## sanity checks
    if output_base < 2 or input_base < 2:
        raise ValueError("Invalid Base")

    for d in digits:
        if d < 0:
            raise ValueError("All digits must be greater than zero")
        if d >= input_base:
            raise ValueError("Digits must be less than or equal to input base")

    if digits == []:
        return []

    if sum(digits) == 0:
        return []

    
    # Conver to base 10 first
    digits.reverse()
    number = sum(digits[x] * (input_base ** x) for x in range(len(digits)))
    # number is now equal to digits in base 10

    output = []

    while True:
        if number / output_base < 1:
            output.append(number)
            break
        
        output.append(number % output_base)
        number = math.floor(number / output_base)

    return list(reversed(output))
