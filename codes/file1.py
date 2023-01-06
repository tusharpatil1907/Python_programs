fname=input("enter file name: ")

print(fname,"before making changes\n")

with open(fname,'r')as f:
    l=f.readlines()
    print(l)

with open(fname,'r')as f:
    print("After capaitalizing first letter of ",fname,"=\n")
    for line in f:
        l=line.title()
        print(l)

"""output:
enter file name: readme.txt
After capaitalizing first letter of  readme.txt =

Hello Guys How Are You All,

Hope You All Are Fine

"""
