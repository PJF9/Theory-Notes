"""
    This Python file is implementing a read work problem, the course enrollment
    of a school. With Object Oriented Programming we can eazily model all the
    problems and implementing them in code. That's why OOP is a usefull tool
    in programming.
"""


class Course:
    pass


class Student:
    def __init__(self, first_name: str, last_name: str, age: int,
                 grade: int, major: list = []):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        self.major = major

    def is_enrolled(self, course: Course) -> bool:
        if self in course:
            return True

        return False

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.age}-{self.grade}-" \
            f"{self.major}"


class Course:
    def __init__(self, course_name, min_grade, max_enrollers):
        self.course_name = course_name
        self.min_grade = min_grade
        self.max_enrollers = max_enrollers
        self.students = []

    def add_student(self, student: Student):
        if (student.grade >= self.min_grade) and (student not in self.students) \
                and (len(self.students) < self.min_grade):
            self.students.append(student)

    def aver_grade(self) -> float:
        n = 0
        for student in self.students:
            n += student.grade

        return n / len(self.students)


course = Course("Fandementals of Computer Science", 17, 3)

student_1 = Student("Petros", "Floratos", 18, 18, ["Comp. Science", "Physics"])
student_2 = Student("Jacob", "Smith", 17, 19, ["Maths", "Art"])
student_3 = Student("Tony", "Joe", 20, 17, ["English"])
student_4 = Student("Marry", "Jonson", 22, 14, ["Maths"])

course.add_student(student_1)
course.add_student(student_2)
course.add_student(student_3)
course.add_student(student_4)

for student in course.students:
    print(student)

print(course.aver_grade())
