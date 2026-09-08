'''file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)

print(file.readline())
file.seek(0)
print(file.readlines())
file.close()'''

'''with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())'''

'''with open('MySql.txt','w') as file:
    file.write('DDL,DML,DCL')'''

'''with open('pfs-63.txt','w') as file:
    file.write('Codegnan')'''


'''with open('pfs-63.txt','a') as file:
    file.write('Institute pfs-63 branch-5')'''

with open('pfs-63.txt','a+') as file:
    file.write(' hlo today in branch-1')
    file.seek(0)
    print(file.read())

with open('pfs-63.txt','r+') as file:
    print(file.read())
    file.write('tom in as usual')
    print(file.read())



