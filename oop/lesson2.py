#example instrance variable
class Triangle:
    def setHeight(self,h):
        #creating instance variable
        self.height = h
    def setBase(self,b):
        #creating instance variable
        self.base = b
    def getArea(self):
        #area is local variable
        area = 0.50 * self.base * self.height
        return area 
    
#create one object
t1 = Triangle()

b = int(input("Enter base"))
t1.setBase(b)

h = int(input("Enter height"))
t1.setHeight(h)

area = t1.getArea()
print(f"area of triangle = {area}")


#create another object 
t2 = Triangle()

b = int(input("Enter base"))
t2.setBase(b)

h = int(input("Enter height"))
t2.setHeight(h)

area2 = t2.getArea()
print(f"area of triangle = {area2}")
