class data1:
    n1=None
    
    def getn1(self):
        self.n1=int(input("enter first no; "))

    def putn1(self):
        print("1st number= ",self.n1)

class data2:
    n2=None

    def getn2(self):
        self.n2=int(input("enter2nd number: "))
    def putn2(self):
        print("2nd number: ",self.n2)
class add(data1,data2):
    ans=None
    def calc(self):
        self.ans=self.n1+self.n2
        print("ans: ",self.ans)

a=add()

a.getn1()
a.getn2()
a.putn1()
a.putn2()
a.calc()
        