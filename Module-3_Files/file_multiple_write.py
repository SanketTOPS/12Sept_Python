"""fl=open('newfile.txt','a')

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")

    fl.write(f"ID:{id}\nName:{name}\n")"""


def getdata():
    fl=open('newfile.txt','a')

    n=int(input("Enter number of students:"))

    for i in range(n):
        id=input("Enter an ID:")
        name=input("Enter a Name:")

        fl.write(f"ID:{id}\nName:{name}\n")
    
getdata()