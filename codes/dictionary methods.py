#Dictionary methods

#dictionary initialization
dict1={
    "Name":"Tushar",
    "roll no":42,
    "branch":"computer",
    "class":"S.Y.Computer"
}
#1 To clear or empty the dictionary. clear() is used.

print("dictionary before deletion: ",dict1)

dict1.clear()
print("dictionary after deletion: ",dict1)

#2 To write an sallow copy of the dictionary. copy() is used.

#dict initialization.
dict2={
    "name":"tushar",
    "class":"sy computer ",
    "roll":42
}

print("dict1: ",dict2)
#this line will copy the dict2 material into dict1.
dict1=dict2.copy()
print("dictionary 2: ",dict1)
#now elements of dict2 are copied in dict1.


#This method creates a new dictionary with specified key and value. fromkeys() is used.

keyset=('key1','key2','key3')
dictionary1=dict.fromkeys(keyset)
print("without value",dictionary1)
dictionary2=dict.fromkeys(keyset,50)

print("with value",dictionary2)

#4 to write the value of specified key. get() is used.

#dict initialization.
print(dict1)
#use of function
print("student name: ",dict1.get("name"))
print("Student roll no: ",dict1.get("roll"))
print("student class: ",dict1.get("class"))

#5 items(): It returns all the key value pair of the dictionary.
#dict initialization.

dictionary3={
    "student1":"Tushar",
    "student2":"Rushikesh",
    "student3":"kalpesh"
}
#EXICUTION 
print("dictionary: ",dictionary3.items())


#6 key(). It returns all keys of the dictionary.

#use previous initialization.

print("dictionary keys: ",dictionary3.keys())

#7. setdefault() This method is used to set a default value to key

print("dictionary: ",dict2)
#below line will print roll no  of student .
x=dict2.setdefault("roll")
print("roll no =",x)
y=dict2.setdefault("name")
print("Name: ",y)

#if specified key is not present it will print none.
z=dictionary3.setdefault("name")
print("it will print none if key is not present: ",z)
#we can also set value to key using setdefault().
a=dictionary3.setdefault("branch","computer")
print("adding in dictionary using setdefault(): ",a)


#8. values() It returns All values of the dictionary.
student={
    "name":"amisha",
    "roll":"305",
    "branch":"computer"
}
print("dictionary values of student dictionary: ",student.values())

#9. update() : This method is updates the dictionary wwith the key values.
print("student info",student)
#updating student info.
student.update({"Branch","computer science"})
print("after updating student info: ",student)

