class  Topten:
    def __init__(self):
        self.num=1

    def  __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            value=self.num
            self.num+=1

            return value
        else:
            raise  StopIteration

values=Topten()
print(next(values))#print(next(values)) prints 1 and also changes the state of the iterator after which num = 2. So the for loop will print the numbers from 2 to 10.
for i in values:
    print(i)