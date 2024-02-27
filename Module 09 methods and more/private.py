class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.phone = phone

    def __get_password(self):
        print(self.__password)
    
    def user_log(self, name, password):
        if name is self.name and password is self.__password:
            return True
        else:
            return False

roni = User('Roni','asdf', '34343434')

# print(roni.__password)
# print(roni.phone)

# roni.__get_password()

result = roni.user_log('roni','asdf')
print(result)