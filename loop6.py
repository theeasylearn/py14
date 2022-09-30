#write a program to findout and display factorial of given number 
#number = 5 => 5 x 4 x 3 x 2 x 1 = 120
#number = 4 => 4 x 3 x 2 x 1 = 24
#number = 3 => 3 x 2 x 1 = 6

number = int(input("Enter number")) #5
result = 1

while number>=1:
    result = result * number
    number = number - 1 #4
print(result)

