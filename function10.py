#example of lambda 
#function-name = lambda input: expression
add = lambda num1,num2 : num1+num2
sub = lambda num1,num2 : num1-num2
mul = lambda num1,num2 : num1*num2
div = lambda num1,num2 : num1/num2 

number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))

result = add(num1=number1,num2=number2)
print(result)

print(sub(num1=number1,num2=number2))
print(mul(num1=number1,num2=number2))
print(div(num1=number1,num2=number2))