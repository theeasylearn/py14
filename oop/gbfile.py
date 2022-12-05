from mbfile import MB
class GB(MB):
    def __init__(self, bytes):
        #calling parent class constructor 
        super().__init__(bytes)
        print("GB class constructor called...")
    def getGB(self):
        # ((bytes / 1024) / 1024) / 1024
        temp = super().getMB() / 1024
        return temp 
