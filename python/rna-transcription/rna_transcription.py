RNA = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
    }

RNA_SET = set(RNA.keys())

def to_rna(value):
    if len(value) > 1:
        if RNA_SET.issuperset(set(value)) is not True:
            return ""
        out = []
        for item in value:
            out.append(_to_rna(item))
        return "".join(out)

    return _to_rna(value)

def _to_rna(value):
    if value not in RNA_SET:
        return ''
    return RNA[value]