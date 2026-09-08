#single inheritance

class whatsappv1:
    def __init__(self,name):
        self.name=name
        print(f"welcone to the whatsapp - v1 {self.name}")
    def messaging(self):
        print('you can send messages')

class whatsappv2(whatsappv1):
    def __init__(self,name):
            self.name=name
            print(f"welcone to the whatsapp - v2 {self.name}")
    def calls(self):
         print("you can do audio and video calls")

reena=whatsappv1("reena")
reena.messaging()
kowsar=whatsappv2("kowsar")
kowsar.messaging()
kowsar.calls()

