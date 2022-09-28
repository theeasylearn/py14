#write a program to print following pattern 
# 10 20 40 80 160 320 ..... 10000

number = 10
multiplier = 2

while number<=10000:
    print(number,end=' ')
    number = number * multiplier #20

