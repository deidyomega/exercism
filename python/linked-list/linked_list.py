class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def pretty_print(self, node=None):
        """ Extra function for debugging, it prints the entire list """
        if node is None:
            node = self.head
        
        print(node.value)
        if node.succeeding is not None:
            self.pretty_print(node.succeeding)

    def push(self, item):
        # if list is blank
        if self.head is None:
            self.head = self.tail = Node(item)
        else: # we already have something            
            new_tail=Node(item, previous=self.tail)
            self.tail.succeeding=new_tail
            self.tail=new_tail

    def pop(self):
        # if there is only one value
        value = self.tail.value
        if not self.tail.previous:
            print("LAST VALUE")
            # reset pointers
            self.tail = None
            self.head = None
            return value

        self.tail.previous.succeeding = None
        self.tail = self.tail.previous
        return value
    
    def shift(self):
        value = self.head.value
        if not self.head.succeeding:
            self.head = None
            self.tail = None
            return value

        self.head.succeeding.previous = None
        self.head = self.head.succeeding
        return value

    def unshift(self, item):
        if self.head is None: # new list
            self.head = self.tail = Node(item)
        else:
            node = Node(item, succeeding=self.head)
            self.head.previous = node
            self.head = node


