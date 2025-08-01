def to_rna(value):
    RNA = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    return "".join([RNA[item] for item in value])
