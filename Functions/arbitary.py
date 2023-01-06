#Arbitary arguments access using *args.
def fruits(*list1):
    for i in list1:
        print("i like ",list1[0])
        print("i like ",list1[1])
        print("i like ",list1[2])
for i in range(3):
    n=input("enter fruits you like: ")
fruits(n)
print(n)
