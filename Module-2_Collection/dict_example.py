stdata={'id':1,'name':'sanket','sub':'python'} #static
#print(stdata)
#print(stdata['name'])
#print(stdata['sub'])
#print(stdata.get('id'))

#print(stdata.keys())
#print(stdata.values())

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""


"""if 'python' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

# ------------------------------------------- #
#print(len(stdata))

print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""


"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} ad Value={j}")"""

stdata['id']=2 #update value
stdata['sub']='iOS' #update value
stdata['city']='Rajkot' #add value
#stdata.pop('id') #delete value
#del stdata['name']
print(stdata)


newdata=stdata.copy()
print(newdata)