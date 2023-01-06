class item:
    icode=0;
    iname="";
    prize=0;
    def __init__(self):
        self.icode=101
        self.iname="Cd"
        self.prize=200
    def putdata(self):
        print(self.icode,self.iname,self.prize)

obj1=item()
obj2=item()

obj1.putdata()
obj2.putdata()
