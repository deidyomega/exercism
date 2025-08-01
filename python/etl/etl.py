def transform(legacy_data):
    output = {}
    for k, v in legacy_data.items():
        for letter in v:
            output[letter.lower()] = k
    return output
