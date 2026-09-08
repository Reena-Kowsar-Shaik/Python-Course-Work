'''class whatsappv1:
    def status(self):
        print("you can add images and videos")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and stickers")
class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can like and you can add reaction")
a=whatsappv3()
a.status()'''

#when u have 2 parents with same method names super method points to single parent
#  if u have two parents we ca go with class method 
class whatsappv1:
    def status(self):
        print("you can add images and videos")
class whatsappv2:
    def status(self):
        print("You can add music and stickers")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can like and you can add reaction")
a=whatsappv3()
a.status()



