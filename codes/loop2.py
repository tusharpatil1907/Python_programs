#for loop
from ast import Num
from itertools import count


num=int(input("enter any number"))
print("table of",num)
for c in range(1,11):
    print(num,'x',c,'=',num*c)