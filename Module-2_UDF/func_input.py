def getdata(id,name):
    print("ID:",id)
    print("Name:",name)


#getdata(1,'Sanket')

n=int(input("Enter number of students"))
for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")

    getdata(id=stid,name=stnm)

