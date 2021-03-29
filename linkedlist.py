class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            return self.students.append(student)
        return -1

    def avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


s1 = Student("Tim", 95)
s2 = Student("Jack", 85)
s3 = Student("John", 90)

c1 = Course('Science', 2)
c1.add_student(s1)
c1.add_student(s3)
print(c1.add_student(s2))

# print(c1.avg_grade())
