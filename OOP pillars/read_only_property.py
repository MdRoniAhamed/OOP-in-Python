class Student:
    def __init__(self, name, id, marks):
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id
    
    @student_id.setter
    def student_id(self):
        self.__id = 32
    
    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


chowdhury = Student('choto chowdhury', 34, 55)

print(chowdhury.student_id)
print(chowdhury.name)
del chowdhury.name
print(chowdhury.name)
