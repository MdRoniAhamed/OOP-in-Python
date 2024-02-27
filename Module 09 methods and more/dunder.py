from typing import Any


class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    
    def __add__(self, other):
        return self.money + other.money

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("hi")

alim = Person('Alim', 12, 343)
dalim = Person('Dalim', 13, 543)


print( alim+dalim)


alim(name="hello")