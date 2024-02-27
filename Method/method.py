# Instance method
# Static method
# Class method
# Abstract method

class School:
    school_name = "ABC School"
    def __init__(self, name) -> None:
        self.name = name

    @staticmethod
    def get_name(name):
        print("My name is Roni")
    @classmethod
    def change_school_name(cls, name):
        cls.school_name = name



# s = School('roni')
# r = School('Emran')

# s.change_school_name('HiFi School')
# # print(s.school_name)
# print(r.get_name('hi'))
        
# Abstract class & method
from abc import ABC, abstractmethod
class Urban(ABC):
    @abstractmethod
    def hi(self):
        print('hello dear friend')
    def hello(self):
        print('This is village')


class Akta(Urban):
    def hi(self):
        super().hi()

akta = Akta()
akta.hello()
