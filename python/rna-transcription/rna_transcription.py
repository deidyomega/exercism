def to_rna(value):
    RNA = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    if set(RNA.keys()).issuperset(set(value)) is not True:
        return ""

    out = ""
    for item in value:
        out += RNA[item]
    return out