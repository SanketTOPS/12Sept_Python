class studinfo:
    def getdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)


st=studinfo()
#st.getdata(101,'Nirav') #static

id=input("Enter ID:")
nm=input("Enter Name:")
st.getdata(id,nm)
