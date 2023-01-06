# renaming the existing module in program
import geometry as geo


# importing whole module 
h=int(input("enter height"))
w=int(input("enter width"))
# using new name of module after renaming
print("area of rectangle: ",geo.rectangle_area(h,w))



side=int(input("enter side of square: "))
print('area of square: ',geo.square_area(side))

radius=int(input("enter radius: "))
print('area of circle: ',geo.circle_area(radius))


