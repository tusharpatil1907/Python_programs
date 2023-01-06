#define base class.
class test1:
    def myfun(self):
        print("base class function")
class test2:
    def myfun(self):
        print("Derived class function")

obj=test2()
obj.myfun()
