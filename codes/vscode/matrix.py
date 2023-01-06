r=int(input("enter number of row"))
c=int(input("enter number of collumn"))

matrix=[]
print("enter number rowwise")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
