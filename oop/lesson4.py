# Example of inheritance 
class Person: #this is parent class
    def walk(self):
        print("I can walk ")
    def eat(self):
        print("I can eat ")
    def read(self):
        print("I can read ")
        
class Student(Person): #this is child class
    def homework(self):
        print("I will write an essay")
    def play(self):
        print("I will play cricket/pubg ")
    def coding(self):
        print("I am learing python ")
        super().read()
        self.homework()
        


p1 = Person()
p1.walk()
p1.read()
p1.eat()
s1=Student()
s1.coding()
s1.play()
s1.homework()
s1.walk()

