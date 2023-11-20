class studinfo:
    #public
    __stid=101 #private
    __stnm='Sanket' #private

    def __getdata(self): #private
        print("This is getdata from studinfo!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)

    def printdata(self): #public
        self.__getdata()

st=studinfo()

#st.getdata()
st.printdata()