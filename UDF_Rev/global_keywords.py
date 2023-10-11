#global
a=34 #1

print("A=",a)

def getvalue():
    global a
    a=68
    print("A=",a)

getvalue()