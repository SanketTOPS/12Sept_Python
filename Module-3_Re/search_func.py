import re

mystr="This is Python!"

x=re.search("This",mystr)
print(x)

if x: #true
    print("Good job!")
else:
    print("Error!")