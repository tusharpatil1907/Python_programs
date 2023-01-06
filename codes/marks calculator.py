m1=float(input("enter marks"))
m2=float(input("enter marks"))
m3=float(input("enter marks"))
total=(m1+m2+m3)
per=total/3
if per>=60 :
    print("first division")
elif per>=50 :
    print("second division")
elif per>=35 :
    print("third division")
else :
    print("you are fail")
    