def flatten(iterable, lst = None):
    if lst is None:
        lst = list()
    for item in iterable:
        if isinstance(item, (list, tuple)):
            lst = flatten(item, lst)
        elif item is not None:
            lst.append(item)
    return lst
