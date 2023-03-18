student={
    "name":"Tushar patil",
    "roll no":42,
    "percent":85.6,
    "branch":"computer"

}
print("length of dictionary",len(student))

#to add items to dictionary.

student["pass/fail"]='pass'
print("dictionary :", student)

#to delete item from dictionary.
student2={
    "Name":"Rushikesh",
    "Roll no":36,
    "Result":34,
    "pass/fail":"fail"
}
print("before deletion",student2)
student2.pop("Roll no")

print('after deletion the roll no will be deleted',student2)

#update items into dictionary.
    #to change value in dictionary.
student3={
    "Name":"Tushar patil",
    "class":"sy",
    "Roll no": 40,
    "percent":79.5
}
print("before updation\n",student3)

student3["percent"]=92.1
student3["class"]="S.Y.Btech comp"
print("After updation\n",student3)

#delete item using del()eyword.

#here we going to delete item from above dictionary.
print("Before deletion\n",student3)
del student3["Roll no"]
print("After deletion\n",student3)
 #the roll no value will be deleted from dictionary.


#To clear whole dictionary we have to use clear() function.

#here we will take first dictionary.

print("before clearing student1; ",student)
#below line will clear whole dictionary.
student.clear()

print("dictionary after deletion:\n",student)

