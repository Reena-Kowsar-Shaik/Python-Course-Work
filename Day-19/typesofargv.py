#positional arguments
'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('reena','reena@gmail.com','reena@123')
display('reena@123','reena@gmail.com','reena')
display('reena@gmail.com','reena@123','reena')'''


#keyword arguments
'''def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='reena',email='reena@gmail.com',password='reena@123')
display(password='reena@123',email='reena@gmail.com',name='reena')
display(email='reena@gmail.com',password='reena@123',name='reena') '''





'''#default arguments
def display(name,email='gmail.com',password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('reena','reena@gmail.com','reena@123')
display('reena','reena@gmail.com')
display('reena')'''


#variable length with positional 
'''def display(*names):
    print(names)

display('reena')
display('reena','kowsar')
display('reena','kowsar','amani')'''

#variable length with keyword
def display(**products):
    print(products)

display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)

