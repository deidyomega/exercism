def rebase(input_base, digits, output_base):
    ## sanity checks
    if output_base < 2 or input_base < 2:
        raise ValueError("Invalid Base")

    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("Invalid Digits")

    if sum(digits) == 0:
        return []

    digits.reverse()
    number = sum(digits[x] * (input_base ** x) for x in range(len(digits)))

    output = []
    while True:
        if number / output_base < 1:
            output.append(number)
            break
        
        output.append(number % output_base)
        number = number // output_base

    return list(reversed(output))
