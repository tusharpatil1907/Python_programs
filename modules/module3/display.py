
from email.policy import default
import input as calc
import operations as op
while True:
    
    ch=input("enter your choice")
    
    if ch=='a':
        print("add= ",op.sum)
    if ch=='s':
        print("sub=",op.sub)
    if ch=='m':
        print("mul=",op.mul)
    if ch=='d':
        print("div=",op.div)
    if ch=='done':
        break
    if ch==default:
        print("invalid enter again")
   
    

