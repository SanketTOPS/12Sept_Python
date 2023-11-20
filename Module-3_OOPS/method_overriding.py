class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)


class otherstuinfo(studinfo):
    def getdata(self, id, name):
        return super().getdata(id, name)



    

st=studinfo()
st.getdata(101,'Sanket')

ot=otherstuinfo()
ot.getdata(102,'Nirav')
