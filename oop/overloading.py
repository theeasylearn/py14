class Box:
    def getArea(self,length=1,width=1):
        area = length * width
        return area 
    def getVolume(self,length=1,width=1,deapth=1):
        volume = length * width * deapth
        return volume
    
b1 = Box()
print(b1.getArea())   #function is called without argument 
print(b1.getArea(10)) #function is called with 1 argument 
print(b1.getArea(10,20)) #function is called with 2 argument 

print(b1.getVolume()) #function is called without argument 
print(b1.getVolume(10)) #function is called with 1 argument 
print(b1.getVolume(10,20)) #function is called with 2 argument 
print(b1.getVolume(10,20,30)) #function is called with 2 argument 
