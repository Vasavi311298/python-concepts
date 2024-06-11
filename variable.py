class car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()

c1.mil=20
c1.wheels=5
car.wheels=10
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)