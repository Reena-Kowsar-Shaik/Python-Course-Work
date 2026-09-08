'''class flipkart:
    products = {'shirts':1000,'handgab':2000,'pants':3000}
    discount=30
    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.addredd = address
        print(f"Hello {self.name} , Welcome to the flipkart")
reena = flipkart()
reena.userinfo('reena',987654321,'hyd')
kowsar = flipkart()
kowsar.userinfo('kowsar',123456789,'bang')'''

class flipkart:
    products = {'shirts':1000,'handgab':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.addredd = address
        print(f"Hello {self.name} , Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{flipkart.discount}% discount is going on, Grab it !")

reena = flipkart()
reena.userinfo('reena',987654321,'hyd')
reena.displaydiscount()
reena.display()
print(reena.products)
print(reena.name)

flipkart.displaydiscount()
flipkart.display()
print(flipkart.products)

#using object ->ins,cls,sta,clsatt
#using class -> cls,sta,clsatt


kowsar = flipkart()
kowsar.userinfo('kowsar',123456789,'bang')
kowsar.displaydiscount()
kowsar.display()