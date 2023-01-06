#factorial of any number using recursion.
def fact(num):
    if num>1:
        return num*fact(num-1)
    else:
        return 1

n=int(input("enter any number: "))

print("factiorial of",n,"is =",fact(n))
