'''try:#it knows error will come or not
    a=int(input())
except:#it handle error
    print("enter the correct datatype")
else:#if not error it execute
    print("a=",a)
finally:#it executes if error or not error
    print("End of the program")
'''
'''try:
    #a=int(input())
    k={1:12,12:13}
    print(k[4])
    l=[234,54]
    print(l[10])
    print(10/0)
    print('1'+1)
except ValueError:
    print('enter the correct dataype')
except KeyError:
    print('Key is not there')
except IndexError:
    print('Index out of range')
except ZeroDivisionError:
    print("can't divide with zero")
except TypeError:
    print('enter the coooreect datatupe')
except NameError:
    print('define the variable')
else:
    print("Error free program")
finally:
    print('end of program')'''

'''try:
    a=int(input())
    k={1:12,12:13}
    print(k[4])
    l=[234,54]
    print(l[10])
    print(10/0)
    print('1'+1)
except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError)as e:
    print("Error ocuured:",e)
else:
    print("Error free program")
finally:
    print("end of the program")'''

'''try:
    #a=int(input())
    k={1:12,12:13}
    #print(k[4])
    l=[234,54]
    print(l[10])
    #print(10/0)
    #print('1'+1)
except Exception as e:
    print('Error occured:',e)
else:
    print('Error free program')
finally:
    print('End of program')'''


try:
    amount=int(input("enter the amount"))
    balance=5000
    if amount<0:
        raise Exception("Amount needs to be positivve")
except Exception as e:
    print('Error occured:',e)
else:
    print('Error free program')
finally:
    print('End of program')
