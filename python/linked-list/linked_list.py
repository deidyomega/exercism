class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        pass


class LinkedList(object):
    
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def shift(self):
        item = self.lst[0]
        del self.lst[0]
        return item

    def unshift(self, item):
        self.lst.insert(0,item)

    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        return iter(self.lst)
