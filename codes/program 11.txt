class sphere():
    def __init__(self,r):
        self.radius=r
    def diameter(self):
        return self.radius*2
    def circumference(self):
        return 2*self.radius*3.14
    def volume(self):
        return 4/3*3.14*self.radius*self.radius*self.radius
n=float(input("Enter radius of sphere: "))
newsphere=sphere(n)
print("Diameter of the sphere: ",newsphere.diameter())
print("Circumference of sphere: ",newsphere.circumference())
print("Volume of sphere: ",newsphere.volume())



"""Output:
Enter radius of sphere: 8
Diameter of the sphere:  16.0
Circumference of sphere:  50.24
Volume of sphere:  2143.5733333333333"""