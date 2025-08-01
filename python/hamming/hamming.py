def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Invalid Length")
    
    return sum([x != y for x, y in zip(dna1, dna2)])
