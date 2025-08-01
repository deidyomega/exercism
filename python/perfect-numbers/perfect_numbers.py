from math import sqrt

def factors(n):
    root = sqrt(n)
    start = int(root)

    # odd numbers aren't divisable by even numbers
    # so we can adjust our step
    if n % 2 == 0:
        step = -1
    else:
        step = -2
        start = start // 2 * 2 + 1

    if root.is_integer():
        yield int(root) 
        start += step # move past the value we already found

    for x in range(start, 0, step):
        if n % x == 0:
            yield x
            yield n // x

def classify(number):
    if number < 1:
        raise ValueError("Number should be greater than 0")
    # slower but more normal
    #val = sum([x for x in range(1, number) if number % x == 0])
    # faster but requires a bit of mathmatical knowhow
    val = sum(list(factors(number))[:-1])
    if val == number:
        return "perfect"
    if val < number:
        return "deficient"
    if val > number:
        return "abundant"
