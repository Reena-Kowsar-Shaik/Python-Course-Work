#positive or negative number
'''n= int(input("Enter a number: "))
if n>0:
    print("The number is positive")
elif n<0:
    print("The number is negative") '''

#even or odd number
'''n= int(input("Enter a number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")'''

#Divisible by 5
'''n= int(input("Enter a number: "))
if n%5==0:
    print("The number is divisible by 5")   
else:
    print("The number is not divisible by 5")   '''

#Divisibility by 5 and 11
'''n= int(input("Enter a number: "))
if n%5==0 and n%11==0:
    print("The number is divisible by 5 and 11")    
else:
    print("The number is not divisible by 5 and 11")  '''

    
'''#check for Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")'''

#check pass or fail
'''marks = int(input("Enter the marks: "))
if marks >= 40:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")'''

'''#check if number is 3-digit number
n = int(input("Enter a number: "))
if 100 <= n <= 999:
    print("The number is a 3-digit number.") '''

#check if character is vowel
'''ch=input("Enter a character: ")  
if ch in "aeiouAEIOU":
    print("The character is a vowel.")
else:
    print("The character is not a vowel.")'''

#check greatest of two numbers
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))  
if n1>n2:
    print(n1,"is greater than",n2)
else:
    print(n2,"is greater than",n1)'''

#check smallest of two numbers
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1<n2:
    print(n1,"is smaller than",n2) '''

#check if number is zero
'''n=int(input('enter a number:'))
if n==0:
    print('number is zero')
else:
    print('number is not zero')'''

#check if number is multiple of 10
''''n=int(input('enter a number:'))
if n%5==0:
    print('number is multiple of 5')
else:   
    print('number is not multiple of 5')'''

#checkif number is multiple of 10
'''n=int(input('enter a number:'))
if n%10==0:
    print('number is multiple of 10')
else:   
    print('number is not multiple of 10')'''

#check if age is eligible to vote
'''age=int(input('enter your age:'))
if age>=18:
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')'''

#check if number is b/w 1 and 100
'''n=int(input('enter a number:'))
if n>=1 and n<=100:
    print('number is b/w 1 and 100')
else:
    print('number is not b/w 1 and 100')'''

#check if number is square of another
'''n=int(input('enter a number:'))
n1=int(input('enter another number:'))
if n==n1*n1:
    print(n,'is square of',n1) 
else:
    print(n,'is not square of',n1) '''

#check if two strings are equal
'''s1=input('enter a string:') 
s2=input('enter another string:')
if s1==s2:
    print('The strings are equal.')
else:
    print('The strings are not equal.')'''

#check if a number is prime
'''n=int(input('enter a number:'))
for i in range(2,n//2+1):
    if n%i==0:
        print(n,'is not a prime number')
        break
else:
    print(n,'is a prime number')'''

#check if number is positive and even
'''n=int(input('enter a number:'))
if n>0 and n%2==0:
    print(n,'is positive and even')'''

#check if character is uppercase
'''ch=input('enter a character:')
if ch.isupper():
    print(ch,'is uppercase')
else:
    print(ch,'is not uppercase')'''

#check if temperature is hot (>30c)
'''temp=int(input('enter temperature:'))
if temp>30:
    print('temperature is hot')'''

#check if a number is a 4-digit even number
'''n=int(input('enter a number:'))
if 1000<=n<=9999 and n%2==0:
    print(n,'is a 4-digit even number') 
else:
    print(n,'is not a 4-digit even number')'''

#check if a character is a consonant
'''ch=input('enter a character:')
if ch.isalpha() and ch not in 'aeiouAEIOU':
    print(ch,'is a consonant')  '''

#check if anumber is divisible by 2 or 3 but not both
'''n=int(input('enter a number:'))
if (n%2==0 or n%3==0) and not (n%2==0 and n%3==0):
    print(n,'is divisible by 2 or 3 but not both')
else:
    print(n,'is not divisible by 2 or 3 but not both')'''

#check if a number is negative and odd
'''n=int(input('enter a number:'))
if n<0 and n%2!=0:
    print(n,'is negative and odd') 
else:
    print(n,'is not negative and odd') '''

#check if a string starts with a vowel
'''ch=input('enter a character:')
if ch[0].lower() in 'aeiou':
    print('starts with vowel')
else:
    print('starts with consonent')'''

#check if three sides form a valid triangle
'''a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print('Valid Traingle')
else:
    print('Invalid Triangle')'''

#find the greatest among three numbers
'''a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print('a is greater')
elif b>c and b>a:
    print('b is greater'')'''

#check if a year ia century year and leap year
'''n=int(input('enter a year'))
if n % 100==0:
    if n % 400 ==0:
        print('century leap year')
    else:
        print('century year')
else:
    if n % 4 == 0:
        print('Leap year')
    else:
        print('Not a leap year') '''

#Check if a character is a digit
'''ch = input()

if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")'''

#check if a number is palindrome
'''n=int(input('Enter a number:'))
temp = n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if n==rev:
    print('palindrome')
else:
    print("Not a palndrome")'''

#compare lengths of two strings
'''s1 = input()
s2 = input()

if len(s1) > len(s2):
    print("First string is longer")
elif len(s2) > len(s1):
    print("Second string is longer")
else:
    print("Both strings are equal")'''

#Check if a number is within range (50 to 100) and divisible by 5
'''n = int(input())

if 50 <= n <= 100 and n % 5 == 0:
    print("In range and divisible by 5")
else:
    print("Condition not satisfied")'''

#Validate if a password is strong (8 or more characters)
''''password = input()

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")'''

'''#Check if sum of two numbers is even
a = int(input())
b = int(input())

if (a + b) % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")'''

#. Check if sum of two numbers is even
'''a= int(input())
b = int(input())

if (a + b) % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")'''

#Check if the character is a special symbol
ch = input()

if not ch.isalnum():
    print("Special character")
else:
    print("Not a special character")