import uuid
from functools import reduce

class Student_det:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.marks = []
        self.total = 0.0
        self.average = 0.0

    def add_marks(self, marks_list):
        self.marks = marks_list
        self.total = reduce(lambda x, y: x + y, marks_list)
        self.average = round(self.total / len(marks_list), 2)

    def get_data(self):
        return f"ID {self.id} | Name: {self.name} | Marks: {self.marks} | Total: {self.total} | Average: {self.average}"

    def display_students(student_list):
        data = map(lambda s: s.get_data(), student_list)

        return list(data)

    def filter_students(student_list):
        data = filter(lambda s: s.average >= 80, student_list)

        return list(data)

    def sort_students(student_list):
        data = sorted(student_list, key= lambda s: s.average, reverse=True)

        return data
    