import re

mystr="This is Python!545646"

#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
x=re.findall('46$',mystr)
print(x)