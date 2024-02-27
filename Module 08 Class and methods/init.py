class Phone:
    # brand = ""
    # price = 0
    # color = ""
    manufacture = "china"
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def send_sms(self, number, text):
        sms = f"Sending sms: {text} {number}"
        return sms
    
my_phone = Phone("OPPO",1200,"red")

print(my_phone.brand)
 