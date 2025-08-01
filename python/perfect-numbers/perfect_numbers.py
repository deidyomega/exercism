def classify(number):
    if number < 1:
        raise ValueError("Number should be greater than 0")
    val = sum([x for x in range(1, number) if number % x == 0])
    if val == number:
        return "perfect"
    if val < number:
        return "deficient"
    if val > number:
        return "abundant"
     