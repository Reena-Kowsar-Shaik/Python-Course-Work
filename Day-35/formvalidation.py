'''import re
fullname=input("Enter your full name: ")
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res= re.fullmatch(pattern,fullname)
print("valid full name" if res else "invalid full name")'''


'''import re
email=input("Enter your email: ")
pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res= re.fullmatch(pattern,email)    
print("valid email" if res else "invalid email")'''


'''import re
phonenumber=input("Enter your phone number: ")
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
res= re.fullmatch(pattern,phonenumber)
print("valid phone number" if res else "invalid phone number")'''


'''import re
password= input("Enter your password: ")
pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res= re.fullmatch(pattern,password)
print("valid password" if res else "invalid password")'''


'''import re
username=input("Enter your username: ")
pattern=r'^[a-zA-Z0-9._]{5,20}$'
res= re.fullmatch(pattern,username)
print("valid username" if res else "invalid username")'''

'''import re
adadhar=input("Enter your Aadhar number: ")
pattern=r'^\d{4}\s\d{4}\s\d{4}$'
res= re.fullmatch(pattern,adadhar)
print("valid Aadhar number" if res else "invalid Aadhar number")'''

import re
pan=input("Enter your PAN number: ")
pattern=r'^[A-Z]{5}\d{4}[A-Z]$'
res= re.fullmatch(pattern,pan)
print("valid PAN number" if res else "invalid PAN number")

