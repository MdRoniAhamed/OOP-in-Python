class Student:
    def __init__(self, name, age, id) -> None:
        self.name = name
        self.age = age
        self.id = id


class Course:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher


class Teacher:
    def __init__(self,name, course) -> None:
        self.name = name
        self.course = course


class School:

    def __init__(self, name, teachers, courses, students) -> None:
        self.name = name
        self.teachers = teachers
        self.students = students
        self.courses = courses


        