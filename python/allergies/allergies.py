class Allergies(object):
    _items = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, number):
        self.number = number

    def is_allergic_to(self, string):
        return bool(self.number & self._items[string])

    @property
    def lst(self):
        return list([x for x in self._items if self.number & self._items[x]])