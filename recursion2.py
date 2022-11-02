# write a program to findout binary of given decimal number 
def DecimalToBinary(number): #number = 7
    reminder = number%2 #0
    number = int(number/2) #4
    if number>0:
        DecimalToBinary(number)
    print(reminder,end='') # 0
        
    
num = int(input("Enter number"))    
DecimalToBinary(number=num)

