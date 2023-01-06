#to short vovels and consonent from string

n=str(input("enter char"))
v=0
c=0
print("string length=",len(n))
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
        v=v+1
    else:
        c=c+1
print("vovels=",v)
print("conconent=",c)

