# Public protected private

class Account:
    pass

class StudentAccount(Account):
    def __init__(self, holder, balance, school) -> None:
        self.__balance = balance
        super().__init__()
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'No money for you'
        self.__balance -= amount
        return amount
    
    def deposit(self, amount):
        if amount < 0:
            return 'Negative amount can not be added'
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
roni = StudentAccount('Roni', 34343, 'CU')

print(roni.get_balance())