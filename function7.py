#example of multiple return value function
def Calculate(number1,number2):
    addition = number1 + number2
    substraction = number1 - number2
    multiplication = number1 * number2 
    division = number1 / number2
    return addition,substraction,multiplication,division

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
result = Calculate(number1=num1,number2=num2) 
print(result)