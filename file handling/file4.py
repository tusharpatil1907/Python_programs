# reading from a file.

fileptr=open(input("enter file name: "),"r")

filedata=fileptr.read()
print("file data: ",filedata)
fileptr.close()

