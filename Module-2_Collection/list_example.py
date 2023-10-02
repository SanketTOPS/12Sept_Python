data=['python','java','php','ruby','angular']
"""print(data)
print(data[0])
print(data[-1])
print(data[0:3]) #slice (range)
print(data[2:])
print(data[:4])"""

"""print(data)
data[1]='android' #update value
print(data)"""

# --------------------------------------------- #
#print(data)

"""for i in data:
    print(i)"""

"""x=data.index('php')
print(x)"""

# 0 - python
# 1 - java
# 2 - php

"""for i in data:
    #print(i)
    print(f"{data.index(i)} - {i}")"""

"""if 'php' in data:
    print("Yes...")
else:
    print("Noo")"""

# --------------------------------- #

print(data)
#print(len(data))
#data.append("c++")
#data.insert(0,'html')
#data.pop()
#data.pop(1)
#data.clear()
#del data[3]
#data.reverse()
#data.sort()
#data.remove('java')
#print(data)

#newdata=data.copy()
#print(newdata)

newdata=['C','C++','DS']
print(newdata)
#print(data+newdata)
data.extend(newdata)
print(data)
