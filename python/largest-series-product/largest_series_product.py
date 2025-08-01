def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Invalide Size")

    return max((
                compute_prod(series[x:x+size])
                for x in range(len(series)-size+1)
    ))

def compute_prod(txt):
    total = 1
    for num in txt:
        total *= int(num)
    return total

