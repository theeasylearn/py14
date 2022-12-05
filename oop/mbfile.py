from kbfile import KB
class MB(KB):
    def __init__(self,bytes):
        #calling parent class constructor 
        super().__init__(bytes) 
        print("MB class constructor called...")
    def getMB(self):
        # (bytes / 1024) / 1024
        temp = super().getKB() / 1024
        return temp 