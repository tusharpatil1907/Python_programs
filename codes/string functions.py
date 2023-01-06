str1=(input("enter anything"))
    ##To check it is alpha numeric or not.
print("This string is alnum=",str1.isalnum())
    ##To check specified string is alphaneumeric or not.
print("This string is aplhanumeric=",str1.isalpha())
    ##To check all character of string is decimal or not.
print("this string is decimal=",str1.isdecimal())
    ##To check  all character of string are digit or not. 
print("this string is digit or not",str1.isdigit())
    ## To check  whether  string is  identifier 
print("this string is valid identifier=",str1.isidentifier())
    ## To check string is in lower case.
print("string is in lower case= ",str1.lower())
    ## To check if string return all characters of string are numeric charecter otherwise false
print("string is numeric =",str1.isnumeric())
    ## To check if all character of string are in upper case or not
print("This string is in upper case=",str1.isupper())
    ## to check if all character of string are havin white spaces
print("This string is havin white spaces=",str1.isspace())
    ## To check length of string.
print("The lenght of string is=",len(str1))
    ## To convert string into lowercase.
print("string in lower case is= ",str1.lower())
    ## To convert string in uppercase.
print("string in upper case= ",str1.upper())\
    ## To convert string from uppercase to lowercase.
print("swapped case of string is=",str1.swapcase())
    ## To remove unwanted whitespaces from string.
print("After removing unwanted whitespaces=",str1.strip())
    ## To remove unwanted white spaces of left side of string.
print("after removing left side whitespaces=",str1.lstrip())
    ## To remove  unwanted whitespaces from right side of string.
print("str after removing unwanted whitespace from right side",str1.rstrip())
    ## To replace old string with new string
print("after replacing string with new one= ",str1.replace(" python","java"))
    ## To break sentence into words.
mylist=str1.split()
print("after breaking string= ",mylist)

