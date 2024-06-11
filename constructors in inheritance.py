class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B:  #The inheritance C(A, B) suggests that C first looks at A and then B. However, B itself already inherits from A. This creates an inconsistency and ambiguity in the inheritance chain, leading to the error.
    def __init__(self):
        super().__init__()#to access the constuctor of superclass i.e A
        print("in B init")

    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is workig")

class C(A,B):

    def __init__(self):
        super().__init__()  # without super it will throw MRO Error (A init will print),it is always from left to right
        print("in C init")

    def feat(self):
        super().feature2()


b1=C()
b1.feat()