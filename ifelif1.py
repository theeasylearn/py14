# concept of if elif decision making statement in python 
'''
    write  a program to accept 5 subject marks from student, calculate total and percentage and display grade as per below creiteria
    percentage      grade
    >80             S
    >70             A
    >60             B
    >50             C
    >40             D
    otherwise       Failed
'''
sub1 = int(input("Enter first subject marks"))
sub2 = int(input("Enter second subject marks"))
sub3 = int(input("Enter third subject marks"))
sub4 = int(input("Enter fourth subject marks"))
sub5 = int(input("Enter fifth subject marks"))
total = sub1 + sub2 + sub3 + sub4 + sub5 #process
percentage = total/5
print(f"total marks = {total} percentage = {percentage}")
if percentage>80:
    print("your grade is S")
elif percentage>70:
    print("your grade is A")
elif percentage>60:
    print("your grade is B")
elif percentage>50:
    print("your grade is C")
elif percentage>40:
    print("your grade is D")
else:
    print("you are failed in exam")

print("Have good day.....")