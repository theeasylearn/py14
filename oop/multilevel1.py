#single level inheritance
class Human:
    def walk(self):
        print("I can walk....")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
    def WhatICanDo(self):
        self.walk()
        self.talk()
        self.eat()
        
class Student(Human):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    #Method Overridding
    def WhatICanDo(self):
        super().WhatICanDo()
        self.read()
        self.write()
        
class Developer(Student):
    def code(self):
        print("I can write code in python")
    def debug(self):
        print("I can debug code in python")
    #Method Overridding
    def WhatICanDo(self):
        super().WhatICanDo()
        self.code()
        self.debug()
    
        
#object-name = className()
d1 = Developer()
d1.WhatICanDo()
