# poly => many
# morph => different

# Overriding

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print('Meaow meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('Bark Bark')

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('ney ney')

don = Cat('don')
don.make_sound()

shepard = Dog('German Shepard')
shepard.make_sound()

manik = Horse('German Shepard')
manik.make_sound()