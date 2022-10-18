#example of function with return value and with argument
def GetSquare(number):
    #temp is local variable, means we can access/change this temp variable only in this function
    temp = number * number 
    return temp 

def GetQube(number):
    #temp is local variable, means we can access/change this temp variable only in this function
    temp = number * number * number
    return temp

num = int(input("Enter number"))
result = GetSquare(num)
print(f"square = {result}")

result = GetQube(num)
print(f"qube = {result}")



