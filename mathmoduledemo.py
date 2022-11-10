import math 
AnyValue = float(input("Enter number"))
print(AnyValue) #3.14
result = math.floor(AnyValue)
print(f"floor value {result}")
result = math.ceil(AnyValue)
print(f"ceil value {result}")
result = math.trunc(AnyValue)
print("truncated value ",result)
result = math.fabs(AnyValue)
print("absolute value ",result)