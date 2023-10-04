tech=['python','java','php','angular','react']
"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[0:3]) #range
print(tech[2:])
print(tech[:3])
print(len(tech))"""

# --------------------------------------------- #
"""if 'php' in tech:
    print("Yes...")
else:
    print("Noo")"""

# --------------------------------------------- #
#print(tech)

"""for i in tech:
    print(i)"""

"""x=tech.index('angular')
print(x)"""

#python - 0
#java - 1

"""for i in tech:
    #print(i)
    print(f"{i} - {tech.index(i)}")"""

"""n=0
for i in tech:
    print(f"{i} - {n}")
    n+=1"""

# --------------------------------------------- #
#List Methods
#print(tech)
#tech[1]='android' #value update
#print(tech)
#tech.append('c++')
#tech.insert(1,'html')
#tech.remove('php')
#tech.pop()
#tech.pop(3)
#del tech[0]
#tech.clear()
#del tech
#tech.reverse()
#tech.sort()
print(tech)

#newtech=tech.copy()
newtech=['c','c++','ds','html']
print(newtech)

#print(tech+newtech)
tech.extend(newtech)
print(tech)
