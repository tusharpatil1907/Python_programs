s1= float (input("Enter the marks of subject 1= "))
s2= float (input("enter marks of s2= "))
s3= float(input("enter marks of s3="))

total=s1+s2+s3
per=total/3
print("total marks of 3 subjects= ",total ,end=' ')
print("/300")
print("percentage= ",per)
print("result=",end=' ')
if per<35:
    print("fail")
if per<80:
    print("pass class")
if per>=80:
    print("distintion")