def is_valid(isbn):
    isbn = list(isbn.replace("-", ""))

    # Needs to be length 10
    if len(isbn) != 10:
        return False
    
    # Except for the last item, all items must be digits
    if not "".join(isbn[:-1]).isdigit():
        return False

    # Last item must be a digit or "X"
    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    if isbn[-1] == "X":
        isbn[-1] = 10

    return sum([((idx+1) * int(num)) for (idx, num) in enumerate(reversed(isbn))]) % 11 == 0
