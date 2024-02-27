class Laptop:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase_age(self, age = 1):
        self.last_increase = self.age
        self.age = age+age

    def repair(self, life_increase=-5):
        self.increase_age(life_increase) 


my_laptop = Laptop("Dell", 1)
print(my_laptop.age)
my_laptop.increase_age(-7)
print(my_laptop.__dict__)