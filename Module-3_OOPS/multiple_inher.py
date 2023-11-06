class nirav:
    nid=0
    nbranch=""

    def n_getdata(self):
        self.nid=input("Enter nirav's ID:")
        self.nbranch=input("Enter nirav's Branch:")
    
class ashok:
    aid=0
    abranch=""

    def a_getdata(self):
        self.aid=input("Enter ashok's ID:")
        self.abranch=input("Enter ashok's Branch:")

class hitesh:
    hid=0
    hbranch=""

    def h_getdata(self):
        self.hid=input("Enter hitesh's ID:")
        self.hbranch=input("Enter hitesh's Branch:")

class college(nirav,ashok,hitesh):
    def printdata(self):
        print("-------Nirav's Data-------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Branch:",self.nbranch)
        print("-------Ashok's Data-------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Branch:",self.abranch)
        print("-------Hitesh's Data-------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Branch:",self.hbranch)



cl=college()
cl.n_getdata()
cl.a_getdata()
cl.h_getdata()
cl.printdata()



