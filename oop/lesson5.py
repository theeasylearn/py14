class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
        
class Employee(Person):
    def __init__(self,salary,post,name,age):
        super().__init__(name,age)
        self.salary=salary
        self.post=post
    
    def display(self):
        super().display()
        print(self.salary)
        print(self.post)
        
# p1=Person('param patel',18)
# p1.display()
ep1 =Employee(80000,'developer','kevat',22)
ep1.display()