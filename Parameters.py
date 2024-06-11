def person(name,age):

    print("name",name)
    print("age:",age)

person('vasavi',25)
#assigning default value
def persons(name,age=18):
    print("name", name)
    print("age:", age)

persons("vasu")#it will automitically assign default age value
persons("vasu",25)#it will over write the default value


#variable length arguments concept
def sum(a,*b):
    c=a
    for i in b:   #int and tuple cann't add , so iterting through loop
        c=c+i
    print("c",c)

sum(23,43,45,67)

#when we dont know what kind of parameters user passing (basically a datatype)

def data(name,*data):
    print("name",name)
    print(data)
data('kaveri',25,'pune',4564567)
#keyword variable legth arguement(kvla)here need to mention keywords
#data('kaveri',age=25,city='pune',mob=4564567)it throws erros as we didnt define key words in function.
#to define keywords **data

def details(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

details('kaveri', age=25, city='pune',mob=4564567)




