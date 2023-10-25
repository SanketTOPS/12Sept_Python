"""fl=open("hello.txt","w")

id=input("Enter an ID:")
name=input("Enter your name:")

fl.write(id)
fl.write(name)
"""


fl=open("hello.txt","a")

id=input("Enter an ID:")
name=input("Enter your name:")

"""fl.write(id)
fl.write(name)"""


fl.write(f"\nID:{id}\nName:{name}")
