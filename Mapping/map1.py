#How to create dictionary 
from stringprep import map_table_b2


map={
    "name":"tushar patil",
    "roll no":300,
    "percentage":86.1
}
print(map)

#To create dictionary using key name.
print("acessing each by key name ")
print("name od student:",map["name"])

#To acess dictionary using get() function.

print('student name: ',map.get("name"))