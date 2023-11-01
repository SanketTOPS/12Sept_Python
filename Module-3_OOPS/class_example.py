class studinfo:
    stid=12
    name="Sanket"

    def myfunc(self):
        print("This is student class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


st=studinfo() #Object of class
print("ID:",st.stid)
print("Name:",st.name)
st.myfunc()
st.getsum(23,45)