import re

mystr="this is Python!6541465416"

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\AThis',mystr)
x=re.findall('446\Z',mystr)
print(x)