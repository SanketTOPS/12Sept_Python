def getdata(id,name):
    print("ID:",id)
    print("Name:",name)


n=int(input("Enter number of students:"))

for i in range(n):
    
    stid=input("Enter your ID:")
    stnm=input("Enter your Name:")

    getdata(stid,stnm) #dynamic
