class item:
    icode=0;
    iname="";
    prize=0;

    def __init__(self,n,c,p):
        self.icode=c
        self.iname=n
        self.prize=p

    def putdata(self):
        print(self.icode,self.iname,self.prize)

obj1=item(101,"cd",100)
obj2=item(102,"dvd",200)  

obj1.putdata()
obj2.putdata()