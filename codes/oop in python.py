


class item:
    icode=0;
    iname="";
    prize=0;
    for i in range(3):
        def getdata(self):
            self.icode=int(input("enter code of item"))
            self.iname=input("enter name of item")
            self.prize=int(input("enter prize of item"))
    for j in range(3):
        def putdata(self): 
           
            print(self.icode,"\t",self.iname,"\t",self.prize)

obj1=item()

#obj2=[item()]

#obj1.getdata()
obj1.getdata()


#obj1.putdata()
obj1.putdata()
