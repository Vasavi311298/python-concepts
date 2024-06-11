def fact(n):
    f = 1
    if(n>0):
        for i in range(1,n):
            f=f*i
        return f
    else:
        print("invalid number")
x=6
result=fact(x)
print(result)