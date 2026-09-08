'''#single level
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")
a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()'''


'''Multilevel Inhertiance
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")
class whatsappv3(whatsappv2):
    def status(self):
        print("You can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.status()'''


'''class whatsappv1:
    def messaging(self):
        print("You can message")


class whatsappv2:
    def calls(self):
        print("You can audio and video calls")


class whatsappv3(whatsappv1, whatsappv2):
    def status(self):
        print("You can add the status for 24 hours")


c = whatsappv3()

c.messaging()
c.calls()
c.status()'''


'''hierarichal
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and video calls")
class whatsappv3(whatsappv1):
    def status(self):
        print("You can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.status()'''



#hybrid
class whatsappv1:
    def messaging(self):
        print("You can message")


class whatsappv2:
    def extracalls(self):
        print("You can add emojis,stickers and gifts")


class whatsappv3(whatsappv1, whatsappv2):
    def calls(self):
        print("You can audio and video calls")


class whatsappv4(whatsappv3):
    def status(self):
        print("you can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.extracalls()

c=whatsappv3()
c.messaging()
c.extracalls()
c.calls()

d=whatsappv4()
d.messaging()
d.extracalls()
d.calls()
d.status()










