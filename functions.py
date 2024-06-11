def greet():
    print("hello Good Morning")
    print("how are you?")

greet()
def add(x,y):#will do a task for you
    c=x+y
    print(c)

add(5,6)

def addition(a,b):# expecting a return value,not responsible to print it
    c=a+b
    return c

result=addition(60,80)
print(result)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
res1,res2=add_sub(9,4)
print(res1,res2)

def update(x):
    print(id(x))
    x=8
    print("x:",id(x))

a=10
update(a)
print(a)
print("a:",id(a))

def update1(lst):
    print(id(lst))
    lst[1]=[8]
    print("lst:",id(lst))

lst=[10,13,17]
update1(lst)
print(lst)
print("lst:",id(lst))




