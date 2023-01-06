class test1:
    x=10
    y=20
    def myfn(self):
        print("this is function1")
    
class test2(test1):
    def myfn2(self):
        print("This is function2")

        print(self.x)
        self.myfn()

obj=test2()
obj.myfn2()

