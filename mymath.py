#module 
def GetSquare(number):
    temp = number * number
    return temp 
def GetQube(number):
    temp = GetSquare(number) * number
    return temp 
def sum(*numbers):
    total = 0
    for item in numbers:
        total=total + item 
    return total 

