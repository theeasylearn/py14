#example of logical operators in python 
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
print(f"num1 = {num1} num2 = {num2} num3 = {num3}")

result = num1==num2 and num2==num3
print(f"{num1} == {num2}  and {num2} == {num3} = {result}")

result = num1==num2 or num2==num3
print(f"{num1} == {num2}  and {num2} == {num3} = {result}")

result = not (num1==num2 and num2==num3)
print(f" not ({num1} == {num2}  and {num2} == {num3}) = {result}")


