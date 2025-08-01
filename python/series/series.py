def slices(series, length):
    if length <= 0:
        raise ValueError("Lenth of second arguement must be greater than 0.")
    if len(series) < length:
        raise ValueError("Length of second arguement must be greater to or equal to the series.")
    if len(series) == 0:
        raise ValueError("First arguement must not be blank.")
    if len(series) == length:
        return [series]
    if length == 1:
        return [x for x in series]

    output = []
    x = 0
    while x < len(series) - length + 1:
        output.append(series[x:x+length])
        x += 1
    return output
