class School:
    def __init__(self,school_name):
        self.school_name = school_name
        print('School init called')

class Grade:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print('Grade Class init called')

class Student():
    def __init__(self, name, school_name, grade_name,):
        self.name = name
        Grade.__init__(self, grade_name)
        School.__init__(self, school_name)
        print('Student init called')


my_school = Student('Roni','City University', '3.90CPA')
print(my_school.school_name)