class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('sam',32)
s2=Student('vasu',3)
lap1=Student.laptop()
s1.show()
s2.show()
lap1=s1.lap
