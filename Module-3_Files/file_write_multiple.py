fl=open('newtest.txt','a')

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter your Name:")

    fl.write(f"\nID:{id}\nName:{name}")

