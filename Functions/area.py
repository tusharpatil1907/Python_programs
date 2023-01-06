#Calculate area of triangle rectangle and circle.

def triangle(b,h):
    
    area=(b*h)/2
    print("area of triangle",area)

def rectangle(l,b):
    area=l*b
    print("area of rectangle",area)

def circle(r):
    area=3.14*r^2

print("*****Enter choice*****")
print("1. area of triangle\n 2. area of rectangle.\n 3. Area of circle.")
a=int(input("enter choice"))
if a==1:
    b=float(input("Enter base of triangle: "))
    h=float(input("Enter height of triangle: "))
    triangle(b,h)
if a==2:
    l=float(input("enter length: "))
    b=float(input("enter breadth: "))
    rectangle(l,b)
if a==3:
    r=float("enter radius: ")
    circle(r)
