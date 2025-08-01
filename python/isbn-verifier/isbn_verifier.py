def is_valid(isbn):
    # Remove dashes
    isbn = list(isbn.replace("-", ""))

    # Needs to be length 10
    if len(isbn) != 10: return False
    
    # Convert last item to 10 if "X"
    if isbn[-1] == "X": isbn[-1] = "10"

    # All items must be digits
    if not "".join(isbn).isdigit(): return False

    return sum([((idx+1) * int(num)) for (idx, num) in enumerate(reversed(isbn))]) % 11 == 0
