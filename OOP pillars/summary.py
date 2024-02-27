class Book:
    def __init__(self, name) -> None:
        self.__name = name

    def read(self):
        raise NotImplementedError
    
    def exercise(self):
        pass

class Physics(Book):
    def __init__(self, name) -> None:
        super().__init__(name)
    

topon = Physics('topon')
# topon.exercise()
# topon.read()

print(topon._Book__name)