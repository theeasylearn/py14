#example of is and not is operators
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

print(f"num1 = {num1} num2 = {num2}")
result = num1 is num2 
result2 = num1 is not num2 
print(f"result = {result} result2 = {result2}")
num1_address = id(num1)
num2_address = id(num2)
print(f"num1 address {num1_address} and num2 address {num2_address}")