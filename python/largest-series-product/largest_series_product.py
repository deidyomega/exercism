def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Invalide Size")
    if size == len(series):
        return compute_prod(series)

    lp = 0
    x = 0
    while x < len(series)-size+1:
        lp = max([lp, compute_prod(series[x:x+size])])
        x += 1
    return lp

def compute_prod(txt):
    total = 1
    for num in txt:
        total *= int(num)
    return total

