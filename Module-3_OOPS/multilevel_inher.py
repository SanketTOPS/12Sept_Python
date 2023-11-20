class nirav:
    nid=0
    nsub=""

    def n_getdata(self):
        self.nid=input("Enter nirav's id:")
        self.nsub=input("Enter nirav's subject:")
    
class sanket(nirav):
    sid=0
    ssub=""

    def s_getdata(self):
        self.sid=input("Enter sanket's id:")
        self.ssub=input("Enter sanket's subject:")

class hitesh(sanket):
    hid=0
    hsub=""

    def h_getdata(self):
        self.hid=input("Enter hitesh's ID:")
        self.hsub=input("Enter hitesh's subject:")

class college(hitesh):
    def printdata(self):
        print("------Nirav's Data------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("------Sanket's Data------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)
        print("------Hitesh's Data------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Subject:",self.hsub)


cl=college()
cl.n_getdata()
cl.s_getdata()
cl.h_getdata()
cl.printdata()