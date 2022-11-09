#example of how to call our own modules
import mymath
number = int(input("Enter number"))
result = mymath.GetSquare(number)
print(f"square is {result}")

result = mymath.GetQube(number)
print(f"qube is {result}")

total = mymath.sum(10,20,30,50,100,200,1000,2000,10000,25000,125000)
print(f"total is {total}")

