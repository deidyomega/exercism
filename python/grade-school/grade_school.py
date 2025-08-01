class School(object):
    def __init__(self):
        self.__lst = {}

    def add_student(self, name, grade):
        self.__lst[name] = grade

    def roster(self):
        grades = sorted(set(self.__lst.values()))
        out = []
        for grade in grades:
            out += self.grade(grade)
        return out

    def grade(self, grade_number):
        return sorted({k: v for k, v in self.__lst.items() if v == grade_number}.keys())
