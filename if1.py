#example of simple if decision making statement 
#write a program to findout qube of given positive number 
number = int(input("Enter positive number to get it's qube"))
if number<0: # < > <= >= == !=
    print("number is negative number so let us convert it into positive number")
    number = 0 - number #process

qube = number * number * number #expression (samikaran) process
print(f"qube is {qube}")
