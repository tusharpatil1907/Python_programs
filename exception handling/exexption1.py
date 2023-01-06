#program with exception.
try:
    print("value of x",a)
except:
    print("an exception occoured")
#eprogram without exception
print("without exception.")
try:
    a=10
    print("value of a is",a)
except:
    print("an error occoured")