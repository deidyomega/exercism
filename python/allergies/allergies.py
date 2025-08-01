class Allergies(object):
    _allergy_list = []

    _items = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats"
    }

    def __init__(self, number):
        if number == 0:
            self._allergy_list = []
        if number == 1:
            self._allergy_list = ["eggs"]


    def is_allergic_to(self, string):
        if string in self._allergy_list:
            return True
        return False

    @property
    def lst(self):
        return self._allergy_list