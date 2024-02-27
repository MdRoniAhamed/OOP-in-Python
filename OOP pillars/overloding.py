# method overloading

def add(num1,num2):
    return num1 + num2

def add(num1,num2, num3=0):
    return num1 + num2 + num3

# result = add(12,13,23)
# print(result)

# Operator overloading

class Account:
    def __init__(self, holder, balance) -> None:
        self.holder = holder
        self.__balance = balance
    
    def __add__(self,other):
        return self.__balance + other.__balance
    
my_account = Account('Roni Ahamed', 34343)
her_account = Account('Emran', 3434)

result = my_account + her_account

print(result)