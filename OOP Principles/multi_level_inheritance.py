class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.license = license 
        self.price = price
    
    def start(self):
        print(f"{self.name} started")
    
class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price):
        self.seat = seat
        self.available_seats = seat 
        self.ticket_price = ticket_price
        super().__init__(name, license,price )

    def sell_ticket(self, customer_name, quantity, amount):
        self.available_seats -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >= 0:
            return Ticket(customer_name)

class ACBus(Bus):
    def __init__(self):
        print('AC Bus created')

class MiniBus(Bus):
    def __init__(self,  name, license, price, seat, ticket_price):
        print('mini bus created')
        super().__init__( name, license, price, seat, ticket_price)


class Ticket: 
    def __init(self, owner):
        self.owner = owner

mini = MiniBus('Mini Mini', 'DK',343434,34,456)
print(mini.name)
