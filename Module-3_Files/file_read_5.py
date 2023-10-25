fl=open('newtest.txt','r+')

print(fl.read())

#print(fl.readline())

#print(fl.readlines())

#print(fl.readlines()[4:6])

"""n=1
for i in fl:
    #print(i)
    print(f"Line:[{n}]={i}")
    n+=1"""

"""if fl.readable():
    print("Yes...File is readable...")
else:
    print("No...File is not readable!")"""

fl.write("\nHello Python!")
