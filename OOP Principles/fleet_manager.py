class BUS:
    owner = 'Ena Transport'

    def __init__d(self, route, license, driver, ):
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = []
    
    def start_trip(self, start_time):
        self.trips.append(start_time)

class Driver:
    def __init__(self, name,mobile, license, address, salary):
        pass

    def drive(self, start, end):
        pass

    def take_vacation(self):
        pass

    def withdraw_salary(self):
        pass

class Passenger:
    def __init__(self,name, mobile, destination):
        pass

    def purchase_ticket(self, destination, money):
        pass

class Manager:
    def __init__(self, name, mobile, department) -> None:
        pass

class Counter:
    def __init__(self, manager, location) -> None:
        pass


