fname=input("enter file name ")
with open(fname,'r')as f:
    print("After capaitalizing first letter of ",fname,"=\n")
    for line in f:
        l=line.title()
        print(l)
f.close()