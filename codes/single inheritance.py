from ssl import ALERT_DESCRIPTION_CERTIFICATE_REVOKED


class data:
    n1=None
    n2=None

    def getdata(self):
        self.n1=int(input("enter first number: "))
        self.n2=int(input("Enter second number: "))

    def putdata(self):
        print("N1= ",self.n1)
        print("N2= ",self.n2)

class add(data):
    ans=None
    def calc(self):
        self.ans=self.n1+self.n2
        print("Ans= ",self.ans)

obj=add()
obj.getdata()
obj.putdata()
obj.calc()


            