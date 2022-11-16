#first example of exception handling mechanism
import sys
try:
    num1 = int(input("Enter 1st number"))
    num2 = int(input("Enter 2nd number"))
    result = num1/num2
    print(f"division = {result}")
except:
    #this block will handle any type of exception 
    
    #print exception detail 
    print(sys.exc_info()[0])  
    print(sys.exc_info())  
finally:
    print("Good bye...")
