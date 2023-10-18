fl=open('temp.txt','a')

id=input("Enter an ID:")
name=input("Enter a Name:")

"""x.write(id)
x.write(name)"""

fl.write(f"ID:{id}\nName:{name}\n")