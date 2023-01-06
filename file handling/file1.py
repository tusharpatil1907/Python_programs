# wriring into file
# write() function is used to write files.

# open
fp=input("enter file name to be created....")
fileptr=open(fp,"w")

fileptr.write(input("enter your content."))
# close.
fileptr.close()
print("Done..")