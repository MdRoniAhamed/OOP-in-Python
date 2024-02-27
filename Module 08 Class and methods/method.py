class Phone:
    color="Black"
    features = ['camera', 'water proof']

    def call(self):
        print("ring ring ring")

    def sent_sms(self,number, text):
        return f"sending sms: {text} to {number}"

my_phone = Phone()

print(my_phone.call())
sms = my_phone.sent_sms(34534,"hello")
print(sms) 