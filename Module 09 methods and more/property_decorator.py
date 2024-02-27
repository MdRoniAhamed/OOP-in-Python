class User:
    def __init__(self,f_name, l_name) -> None:
        self.first = f_name
        self.last = l_name
        self.email = f"{self.first}.{self.last}@user.com"

    def email(self):
        return 
mark = User("mark","zuku")
print(mark.first)
print(mark.last)
print(mark.email)
