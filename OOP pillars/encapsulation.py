class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder 
        self._account_number = 165
        self.__balance = initial_balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
class StudentAccount(Account):
    def __init__(self,school, holder, initial_balance):
        self.school = school
        super().__init__(holder, initial_balance)

rafsan = StudentAccount('City University', 'rafsan', 300)
# print(rafsan.__balance)
rafsan.deposit(3434)
rafsan.deposit(3434)
rafsan.deposit(3434)
# print(rafsan.__balance)
print(rafsan._Account__balance)
rafsan._account_number = 145
rafsan._Account__balance = 0
print(rafsan._account_number)



