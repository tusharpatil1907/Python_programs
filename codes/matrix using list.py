r= int(input("enter number of rows"))
c= int(input("enter number of columns"))

a=[]
print("enter number by row")
for i in range(r):
    b=[]
    #a.append(int(input()))
    for j in range(c):
        b.append(int(input()))
    a.append(b)
print("output:")
for i in range(r):
    for j in range(c):
        print(a[i][j],end=' ')
    print()
