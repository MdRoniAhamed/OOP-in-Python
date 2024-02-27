from abc import ABC, abstractmethod

# abstract base class
class Man:
    pass

class Animal(ABC):

    @property
    @abstractmethod
    def eat(self,name, hello):
        self.name = name

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        print('moving around in the zoon')




class Monkey(Animal, Man):
    def __init__(self) -> None:
        self.__name = 'Monkey' 
    # @property
    def sing(self):
        print("monkey is singing")
    
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self, name):
        print("Eating banana")
    
    def move(self):
        print('hanging on the branches of the trees')
        return super().move()

layka = Monkey()
print(layka)
print(layka.sing())
layka.eat('hello')
layka.name = 'Moonkay'
print(layka.name)
