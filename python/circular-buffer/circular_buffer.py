class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._read_pointer = 0
        self._write_pointer = 0
        self._data = [None] * self.capacity

    def read(self):
        data = self._data[self._read_pointer]
        if data is None:
            raise BufferEmptyException("Buffer Empty")
        
        self._data[self._write_pointer] = None
        self._read_pointer = (self._read_pointer + 1) % self.capacity

        return data


    def write(self, data):
        if self._data[self._write_pointer] is not None:
            raise BufferFullException("Buffer Full")
        self._data[self._write_pointer] = data
        self._write_pointer = (self._write_pointer + 1) % self.capacity

    def overwrite(self, data):
        # if they are the same, we need to move the read pointer,
        # to match the write pointer (when it increments in a second)
        if self._write_pointer == self._read_pointer:
            self._read_pointer = (self._read_pointer + 1) % self.capacity

        self._data[self._write_pointer] = data
        self._write_pointer = (self._write_pointer + 1) % self.capacity

    def clear(self):
        self._data = [None] * self.capacity

