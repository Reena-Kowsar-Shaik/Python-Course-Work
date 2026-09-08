from abc import ABC,abstractmethod

class Phonepay(ABC):
    def senderinfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("you need to enter the pin")
    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepay):
    def transaction(self):
        print("payment using hdfc")
class SBI(Phonepay):
    def transaction(self):
        print("payment using SBI")
class UNION(Phonepay):
    def transaction(self):
        print("payment using union")
class AXIS(Phonepay):
    def transaction(self):
        print("payment using union")
class ICIC(Phonepay):
    def transaction(self):
        print("payment using union")

reena = HDFC()
reena.senderinfo()
reena.amount()
reena.pin()
reena.transaction()


