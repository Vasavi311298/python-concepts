from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("It's running")

class Whiteboard(Computer):
    def process(self):
        print("It's writing")

# com = Computer()  # This line will raise an error because we cannot instantiate an abstract class
lap = Laptop()
wh = Whiteboard()

lap.process()  # This will print "It's running"
wh.process()   # This will print "It's writing"
