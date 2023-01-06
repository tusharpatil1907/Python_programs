class data:
    n1=None
    n2=None

    def getdata(self):
        self.n1=int(input("enter number 1: "))
        self.n2=int(input("enter number 2: "))
    def putdata(self):
        print("n1= ",self.n1)
        print("n2= ",self.n2)

class add(data):
    ans=None
    def calc(self):
        self.ans=self.n1+self.n2

class output(add):
    def show(self):
        print("ans= ",self.ans)

obj=output()
obj.getdata()
obj.putdata()
obj.calc()
obj.show()