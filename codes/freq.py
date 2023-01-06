str1=input("Enter string: ")
list1=[]
list1=str1.split()
freq=[list1.count(p) for p in list1]
print("The frequency of word is: ")
print(dict(zip(list1,freq)))

