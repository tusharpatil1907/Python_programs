#Program to check if a substring is present in a given string.
str=input("Enter string: ")
str2=input("Enter substring to find in string: ")

if(str.find(str2)==-1):
    print("Substring not found")
else:
    print("Substring is found")

