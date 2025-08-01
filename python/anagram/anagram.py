def detect_anagrams(string, array):
    string = string.lower()
    tester = sorted(list(string))

    output = []
    for item in array:
        if item.lower() == string:
            continue
        if tester == sorted(list(item.lower())):
            output.append(item)

    return output