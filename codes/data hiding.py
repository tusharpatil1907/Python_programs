class test1:
    __x=10
    y=20
    def myfn1(self):
        print("this is function1")
class test2(test1):
    def myfn2(self):
        print("This is function 2")
        print(self.x)
        self.mtfn1()
obj=test2()
obj.myfn2()