# appending to a file.
# in this we are going to add mode data in existing file.
f=input("enter file name to be entered: ")
# "a " for append mode.
fileptr=open(f,"a")
fileptr.write(input("enter content to add: "))
fileptr.close
