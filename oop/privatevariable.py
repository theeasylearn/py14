class Account:
    def __init__(self,name,balance):
        self.name = name #public instance variable
        self.__balance = balance #private instance variable 
    def display(self):
        print("name ",self.name)
        print("balance ",self.__balance)
        
a1 = Account("Ankit Patel",5000000000)
a2 = Account("Jiya Patel",8000000000)

a1.display()
a2.display()
a1.name = "Ankit M Patel"
a2.name = "Jiya A Patel"

a1.display()
a2.display()

a1.__balance = 99999999999 #will be ignored
a1.display()

print("Good bye...")