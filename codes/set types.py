#create set 
str_set={"apple","oriange","mango"}
int_set={2,4,3,6,7,8}
float_set={2.3,4.5,3.1,5.1}
mixed_set={1,"tushar",1.5,}

print("string set: ",str_set,"\n int set: ",int_set,"\n Float set",float_set,"\n Mixed set: ",mixed_set)

#acess value of set.

fruit_set={"apple","mango","oriange"}
print(fruit_set)

#update item of set
#we cannot update in set it will generate error.

#length of set using len().

print("set length=",len(fruit_set))

#add items in set using add().
fruit_set.add("pineapple")
print("updated set=",fruit_set)

#add multiple items using single function. 
print("before updating",mixed_set)
mixed_set.update(["patil",29,8.9,"shahada"])
print("after updating",mixed_set)

#delete item from set using remove() function.

print("set before removeing items: ",fruit_set)
#below line will remove specific item from set.
fruit_set.remove("pineapple")
print("after removing: ",fruit_set)

#delete set using using discard() 

set0={"tushar","patil","shahada"}
print("before removing",set0)
#below line will discard whole set.
set0.discard("shahada")
print("after discarding",set0)

#join 2 sets.

set1={"apple","oriange","mango"}
set2={"cherry","grapes","melon"}
#below line will join both sets. union() is used.
set3=set2.union(set1)

print("after adding both set",set3)

#program to search particular element in set.

print("before",fruit_set)
