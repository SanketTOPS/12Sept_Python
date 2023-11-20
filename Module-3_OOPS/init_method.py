class studinfo:
    """def __init__(self):
        print("This is init method in python!")"""

    def __init__(self,stid,stnm) -> None:
        print("ID:",stid)
        print("Name:",stnm)
    
    def getsum(self,a,b):
        print("Sum:",a+b)


st=studinfo(101,'Nirav')
st.getsum(12,34)

