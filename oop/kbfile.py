class KB:
    def __init__(self,bytes):
        self.bytes = bytes 
        print("KB class constructor called....")
    def getKB(self):
        temp = self.bytes / 1024
        return temp 