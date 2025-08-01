class Garden(object):
    plant_key = {
        "V": "Violets",
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes"
    }
    def __init__(self, diagram, students=
        ["Alice", "Bob", "Charlie",
        "David", "Eve", "Fred",
        "Ginny", "Harriet", "Ileana",
        "Joseph", "Kincaid", "Larry"]
    ):
        self.students = sorted(students)
        self.r1 = diagram.splitlines()[0]
        self.r2 = diagram.splitlines()[1]

    def plants(self, student):
        index = self.students.index(student) * 2
        plants = self.r1[index:index+2] + self.r2[index:index+2]
        return [self.plant_key[x] for x in plants]

