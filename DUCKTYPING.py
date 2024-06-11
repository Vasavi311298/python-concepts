'''class duck:
    def sound(self):
        print('quak quak')

class dog:
    def sound(self):
        print('bow bow')

class cat:
    def sound(self):
        print('meow meow')

def All_sound(obj):
    obj.sound()

x=cat()
All_sound(x)'''

class Pycharm:
    def execute(self):
        print('compiling')
        print('runing')

class Myeditor:
    def execute(self):
        print('spell check')
        print('conversion check')
        print('compiling')
        print('runing')

class laptop:
    def code(self,ide):
           ide.execute()

ide = Pycharm() #Myeditor()

lap1 = laptop()
lap1.code(ide)
