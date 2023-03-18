
class item:
    iname="";
    icode=0;
    prize=0;
    qty=0;
    amount=0;   
    def getdata(self):
        self.icode=int(input("enter code of item: "))
        self.iname=input("enter name of product: ")
        self.prize=int(input("enter prize: "))
        self.qty=int(input("enter qty: "))
        self.amount=self.prize*self.qty

    def putdata(self):
        print(self.icode,"    ",self.iname,"\t",self.qty,"\t",self.prize,"\t",self.amount)
total=0
qty_total=0
obj1=item()
obj2=item()
#obj3=item()

obj1.getdata()
obj2.getdata()

print("code\tname\tqty\tprize\tamount")
obj1.putdata()
obj2.putdata()
qty_total=obj1.qty+obj2.qty
total=obj1.amount+obj2.amount
print("total quantity",qty_total ,"\t Total amt= ",total)

