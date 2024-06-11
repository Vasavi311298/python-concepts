class A:
    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B(A):
    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is workig")

class C(B):#multilevel inheritance  #C(A,B) then multiple inheritance :multilvel and multiple both cannt use at a time
    def feature5(self):
        print("feature 5 is working")

a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
b1.feature3()
b1.feature4()
c1=C()
c1.feature1()
c1.feature3()