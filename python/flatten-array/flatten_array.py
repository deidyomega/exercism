def flatten(iterable):
    lst = list()
    for item in iterable:
        if isinstance(item, (list, tuple)):
            lst += flatten(item)
        elif item is not None:
            lst.append(item)
    return lst
