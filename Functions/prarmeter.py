def add(a=2,b=3):
    x=a
    y=b
    ans=x+y
    print("addition= ",ans)

x=int(input("enter 1st number"))
y=int(input("enter second number"))
print("with argument")
add(x,y)

print("without argument")
add()