#to excess value of set
set1={"apple","oriange","mango"}
print("fruit set: ",set1)

#you cannot update set.

#length  of set.
#len()function is used.
print("length=",len(set1))

#add item to set.
print(set1)
set.add("cherry")

#add more than one.

set1.update("mango","pineapple")
print(set1)

#delete item from set using remove().
set2={"apple","oriange","mango"}
print("before deletion" ,set2)

set2.remove("oriange")

print("After deleting oriange",set2)

#delete item from set using discard() function.

print("before discarding",set2)
set2.discard("oriange")



