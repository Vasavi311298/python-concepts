x=int(input("enter a number"))
r=x%2
if(r==0):
    print("x is even number")
    if(x>5):
        print("great")
    else:
        print("low")
elif x>10:
    print("x is greater than 10")
else:
    print("wrong input")