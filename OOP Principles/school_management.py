class School:
    def __init__(self,name, address, principal = ''):
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)
    
    def remove_grade(self, name):
        id = 0
        for i,grade in enumerate(self.grades):
            if grade.name == name:
                idx = id
        del self.grades[idx]
    

class Grade:
    def __init__(self,name, teacher):
        self.name = name
        self.students = []
        self.teacher = teacher
    
    def __repr__(self):
        return f"{self.name} with teacher {self.teacher}"
    
    def __del__(self):
        print(f"DEleting{self.name} with teacher{self.teacher}")
    


oxford = School('Oxford Kid Academy', 'Mirpur', 'Obayed Alam')
oxford.add_grade("class 3", "Osman Gani")
oxford.add_grade("class 5", "Nasma mam")
print(oxford.grades)
oxford.remove_grade('class 3')
print(oxford.grades)