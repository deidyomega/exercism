class InputCell(object):
    def __init__(self, initial_value):
        self.value = initial_value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value + other
        else:
            self.value = self.value + other.value
        return self.value

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value - other
        else:
            self.value = self.value - other.value
        return self.value

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value * other
        else:
            self.value = self.value * other.value
        return self.value

    def __div__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value / other
        else:
            self.value = self.value / other.value
        return self.value
    

class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.compute_function = compute_function
        self.inputs = inputs
        self.value = 0
    
    def get_value(self):
        """ Lazy compute when value is requested """
        print("hitting getter")
        self._value = self.compute_function(self.inputs)
        return self._value

    def set_value(self, value):
        self._value = value

    value = property(get_value, set_value)

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value + other
        else:
            self.value = self.value + other.value
        return self.value

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value - other
        else:
            self.value = self.value - other.value
        return self.value

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value * other
        else:
            self.value = self.value * other.value
        return self.value

    def __div__(self, other):
        if isinstance(other, (int, float)):
            self.value = self.value / other
        else:
            self.value = self.value / other.value
        return self.value

#def test_compute_cells_can_depend_on_other_compute_cells(self):
input_ = InputCell(1)
times_two = ComputeCell([input_], lambda inputs: inputs[0] * 2)
times_thirty = ComputeCell([input_], lambda inputs: inputs[0] * 30)
output = ComputeCell(
    [times_two, times_thirty],
    lambda inputs: inputs[0] + inputs[1]
)

print(output.value, 32)
input_.value = 3
print(output.value, 96)
