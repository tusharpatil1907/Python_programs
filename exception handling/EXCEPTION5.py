try:
    a=10
    b=0
    c=a/b
    print("value of c:",c)
except:
    print("dont put zero in denominator")
else:
    print("This is else statement")
finally:
    print("This is finally block")