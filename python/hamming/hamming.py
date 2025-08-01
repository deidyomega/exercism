def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError
    
    count = 0
    for d1, d2 in zip(dna1, dna2):
        if d1 != d2:
            count += 1
    return count