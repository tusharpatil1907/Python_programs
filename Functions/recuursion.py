#recursion: table of 5 using recursion.

def table(num):
    if num<=50:
        print(num,end=" ")
        num=num+5
        #function used to call by itself
        table(num)
table(5)
