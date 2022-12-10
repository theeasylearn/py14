class Book:
    #class variable 
    publisher = "sunshine publisher"
    def __init__(self,name,price):
        #instance variable
        self.name = name
        self.price = price 
    def display(self):
        print('book name ', self.name)
        print('book price ', self.price)
        print('publisher name ',Book.publisher)
        print("-"*100)
    def setPublisher(self,publishername):
        #always change class variable only using class name 
        Book.publisher = publishername
b1 = Book('secret',600)
b2 = Book('the atomic habit',500)
b1.display()
b2.display()
b1.setPublisher('MoonLight Publisher')
b1.display()
b2.display()