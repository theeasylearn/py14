class Box:
    #constructor
    def __init__(self,length,width=1,deapth=1):
        print("constructor called....")
        #create instance variable 
        self.length = length
        self.width = width 
        self.deapth = deapth
    def getArea(self):
        #creating local variable area 
        area = self.length * self.width
        return area 
    def getVolume(self):
        volume = self.length * self.width * self.deapth
        return volume 

l = int(input("enter length"))

#creating object 
#objectname = class()
b1 = Box(length=l)

area = b1.getArea()
print(f"box area = {area}")

volume = b1.getVolume()
print(f"box volume = {volume}")