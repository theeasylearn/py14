#write a program to do addition, substraction, multiplication, division of two given input
num1 = input("Enter first number")
num2 = input("Enter second number")
#convert string into integer 
num1=int(num1)
num2 = int(num2)

#addition substraction multiplication division 
#process => expression (samikaran)
add = num1+num2 #it will create variable add and store addition of num1 and num2 in it 
sub = num1-num2
mul = num1*num2
div = num1/num2 

print("addition = ",add)
print("substraction = ",sub)
print("multiplication = ",mul)
print("division = ",div)