class items:
    iname="";
    icode=0;
    prize=0;
    qty=0;
    def getdata(self):
        self.icode=int(input("enter item code: "))
        self.iname=input("enter name of item: ")
        self.prize=int(input("enter prize"))
        self.qty=int(input("enter quantity"))

    def putdata(self):
        print(self.icode,self.iname,self.prize,self.qty)

size=int(input("enter no of items to be entered: "))
total=0
itemlist=[]
i=0

while i<size:
    itemlist.append(items())
    i=i+1

for i in itemlist:
    i.getdata()
for i in itemlist:
    i.putdata()
for i in itemlist:
    total=total+i.prize
print("total amt: ",total)
