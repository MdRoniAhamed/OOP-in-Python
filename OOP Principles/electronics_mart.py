
class Laptop:
    def __init__(self,brand, price, color, disc_size):
        self.brand = brand
        self.price = price 
        self.color = color 
        self.disc_size = disc_size
    
    def run(self):
        print("running the laptop")
    
    def purchase(self, money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print("this device is for you")
            return money - self.price


class Phone:
    def __init__(self, brand, price, color, camera, sim_num) -> None:
        self.brand = brand 
        self.price = price 
        self.price = price 
        self.camera = camera
        self.sim_num = sim_num

    def is_dual_sim(self):
        return self.sim_num > 1


class Watch:
    def __init__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price 
        self.color = color
        self.watch_type = watch_type
    
    def is_digital(self):
        return self.watch_type == 'digital'


class Manager:
    def __init__(self, name, salary, experience, designation) -> None:
        
        pass

