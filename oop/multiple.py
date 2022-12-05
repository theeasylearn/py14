# real world example of multiple inheritance
class KB:
    def __init__(self,bytes):
        self.bytes = bytes 
        print("KB class constructor called....")
    def getKB(self):
        temp = self.bytes / 1024
        return temp 
class MyMath:
    def getRoundValue(self,number,precision=2):
        temp = round(number,precision)
        return temp 
    
class MB(KB,MyMath):
    def __init__(self,bytes):
        #calling parent class constructor 
        super().__init__(bytes) 
        print("MB class constructor called...")
    def getMB(self):
        # (bytes / 1024) / 1024
        temp = super().getKB() / 1024
        return super().getRoundValue(temp) 
class GB(MB):
    def __init__(self, bytes):
        #calling parent class constructor 
        super().__init__(bytes)
        print("GB class constructor called...")
    def getGB(self):
        # ((bytes / 1024) / 1024) / 1024
        temp = super().getMB() / 1024
        return super().getRoundValue(temp)  

b = int(input("Enter bytes "))
g1 = GB(bytes = b)

kilobytes = g1.getKB()
megabytes = g1.getMB()
gigabytes = g1.getGB()

print(f"Kilobytes = {kilobytes}  megabytes = {megabytes} gigabytes = {gigabytes}")
