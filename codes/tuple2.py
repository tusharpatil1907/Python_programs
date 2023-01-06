#to calculate length of tuple
tuple=("banana","apple","mango")
print("length of tuple is= ",len(tuple))

#you cannot add item to tuple 
#to add item to tuple first convert to list then add and convert back to tuple.

#delete item from tuple 
#deleting item is not possible in tuple.
#simple you have to use "del" keyword to delete completely.
tuple2=("tushar","patil","shahada") 
print("before updation= ",tuple2)
del tuple2;
print("value remain after deletion= ",tuple2)

#joint two tuples.
#to join two tuples simple use(+)operator.

add_tuple=("guawa",'kivi','pineapple')
print("tuple 1= ",tuple)
print("tuple 2= ",add_tuple)
    #now add tuple.
sum_tuple=tuple+add_tuple
print('addition of tuple= ',sum_tuple)
