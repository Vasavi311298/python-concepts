class computer:
    def __init__(self):
        self.name='vasavi'
        self.age=25
    def update(self):
        self.age=30

    def compare(self,other):
        if self.name == other.name:
            return True
        else:
            return False

c1=computer()
c2=computer()

c1.update()
if c1.compare(c2):
    print("thye are same")
else:
    print("thye are not same")
print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
