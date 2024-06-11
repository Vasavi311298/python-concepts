a=10 #global variable
print(id(a))
def summary():
    a=9  #if want to change global variable without affecting the local variable globals()
    x=globals()['a']
    print(id(x))
    globals()['a']=20
    print(x)
    #global a #if want to change the global variable
    #a=15
    print("in fun",a)

summary()

print("outside",a)