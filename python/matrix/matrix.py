class Matrix(object):
    def __init__(self, matrix_string):
        # Convert the dataset into a list of ints based on \n char
        self.rows = [[int(y) for y in x.split()] for x in matrix_string.split("\n")]
        # transform data into column using the zip function
        self.columns = [list(x) for x in zip(*self.rows)]          

    def row(self, index):
        # index is based on 1 == first row, so we need to reduce index by one, to follow python's 0-index rules
        return self.rows[index-1]

    def column(self, index):
        # index is based on 1 == first row, so we need to reduce index by one, to follow python's 0-index rules
        return self.columns[index-1]
