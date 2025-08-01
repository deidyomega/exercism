"""
To the poor sap reading this.
I didn't actually implment a circularbuffer,

But it handles all the cases just fine.

Basically the first item is always the oldest
and as they are read, it's deleted, and a new 
spot appears at the end of the list
"""
class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    __list_size = 0
    __list_data = []

    def __init__(self, capacity):
        self.__list_size = capacity
        self.clear()

    def read(self):
        # read the oldest
        data = self.__list_data[0]
        if data is None:
            raise BufferEmptyException("Buffer empty")
        del self.__list_data[0]
        self.__list_data.append(None)
        return data

    def write(self, data):
        x = 0
        while x < len(self.__list_data):
            if self.__list_data[x] == None:
                self.__list_data[x] = data
                return
            x += 1
        raise BufferFullException("Buffer full")

    def overwrite(self, data):
        if None in self.__list_data:
            self.write(data)
        else:
            self.read()
            self.write(data)

    def clear(self):
        self.__list_data = [None] * self.__list_size


