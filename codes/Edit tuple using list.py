#Make changes in tuple using list..
fruit_tuple=('apple','banana','mango')
print('stock ',fruit_tuple)
list1=list(fruit_tuple)
print('after converting to list= ',list1)
#for replacing
n=int(input("enter position to replace "))
list1[n]=input("reppalce= ")
print('after replacement',list1)
#for adding.
add=int(input("enter number of items to add= "))
for i in range (0,add):
    list1.append(input("enter item to add="))
print()
print('after adding =',list1)
fruit_tuple=tuple(list1)
print('after converting',fruit_tuple)