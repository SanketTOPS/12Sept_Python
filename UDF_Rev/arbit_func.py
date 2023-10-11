"""def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

getdata(101,'Sanket','Python')"""


def getdata(*data): #arbit arguments (tuple)
    print("ID:",data[0])
    print("Name:",data[1])
    print("Subject:",data[2])


getdata(101,'Sanket','Python')