import random
import datetime

fl=open('stdata.txt','a')

n=int(input("Enter number of Students:"))

for i in range(n):
    id=random.randint(111,999)
    cdate=datetime.datetime.now()
    name=input("Enter your name:")

    fl.write(f"\nDate:{cdate}\nID:{id}\nName:{name}")

