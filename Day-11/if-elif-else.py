n=int(input())
if n>10000:
    print('Trip')
elif n>5000:
    print('Resort Stay')
elif n>3000:
    print('Movie and Dinner')
elif n>1000:
    print('Cafe and Shopping')
elif n>500:
    print('Street food and Park Visit')
else:
    print('Stay Home')