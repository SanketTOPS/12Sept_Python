import re

mystr="This is Python!"

x=re.search('python',mystr)
print(x)

if x: #true
    print("Match done!")
else:
    print("Error!")