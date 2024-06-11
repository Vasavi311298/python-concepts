class student:
    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return  self.m1
    def set_m1(self,value):
        self.m1=value

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def information():
        print("this is static method")


s1=student(12,34,23)
s2=student(12,34,23)
s1.avg()
s1.m1=50
s1.get_m1()
s2.set_m1(90)
student.information()
print(s1.m1,s2.m2,s1.avg())
print(s2.set_m1(90),s1.get_m1(),s2.m1)
print(student.info(),student.information())