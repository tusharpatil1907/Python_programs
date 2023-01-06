#Program to map two lists into dictionary.
keys=[]
val=[]
n=int(input("Enter number of elements of dictionary: "))
print("for keys")
for x in range(0,n):
  #  ele=(int(input("Enter element" +str(x+1)+ ": "))
    keys.append(int(input("Enter keys: ")))
print("For values")
for x in range(0,n):
 #   ele=int(input("Enter element" +str(x+1)+ ": "))
    val.append(int(input("Enter element: ")))
d=dict(zip(keys,val))
print("The dictionary is: ", d)
