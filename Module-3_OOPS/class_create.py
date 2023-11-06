class studinfo:
    stid=12
    stnm='Sanket'

    def myfunc(self):
        print("This is myfunc.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


# Object of Class
st=studinfo()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
st.getsum(34,67)