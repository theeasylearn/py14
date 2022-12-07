# Example of hierarchical inheritance 
class Shape:
    def getpi(self):
        return 3.1415
    def getsquare(self,number):
        return  number * number
    
class Circle(Shape):
    def __init__(self,number):
        self.number = number
    def  getarea(self):
        #pi * radius * radius
        temp = super().getpi() * super().getsquare(self.number)
        return temp 
    
class Cyliender(Shape):
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def getarea(self):
        answer = (2* super().getpi() * self.radius * self.height ) + (2 * super().getpi() * super().getsquare(self.radius))
        return answer
    
print("""Enter 1 for circle
Enter 2 for cylinder """)
option = int(input("Enter your choice "))

if option==1:
    radius=int(input("Enter value for radius "))
    c1 = Circle(radius)
    area=c1.getarea()
    print("area of circle is = ",area)
    
elif option==2:    
    radius=int(input("Enter value for radius "))
    height=int(input("Enter value for height "))
    c2 = Cyliender(radius,height)
    area = c2.getarea()
    print("area of cyliender = ",area)
else:
    print("invalid choice ")