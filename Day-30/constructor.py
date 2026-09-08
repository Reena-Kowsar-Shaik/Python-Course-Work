#it is called automatically when an object is created ---Constructor

'''class flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"hello  {self.name}, Welcome to the flipkart")
reena=flipkart('reena',12345678987)
kowsar=flipkart('kowsar',8765432321)'''

class instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)
reena = instagram('reena','reena@123')
reena.display()
print(reena.username)
print(reena.getpassword())
print(reena.accesspost)

reena.username='reena'
reena.setpassword('reena@123')
reena.accesspost="sunset.png"
reena.accesspost='forest.png'
print(reena.username)
print(reena.getpassword())
print(reena.accesspost)