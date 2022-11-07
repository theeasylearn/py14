#example of how to call our own modules
import mymath
number = int(input("enter number"))
square = mymath.GetSquare(number)
print(f"square of given number is {square}")

qube = mymath.GetQube(number)
print(f"qube of given number is {qube}")

total = mymath.sum(10,20,30,40,50,100)
print(f"total of given number is {total}")

