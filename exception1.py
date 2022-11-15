#first example of exception handling mechanism
try:
    num1 = int(input("Enter 1st number"))
    num2 = int(input("Enter 2nd number"))
    result = num1/num2
    print(f"division = {result}")
except ValueError:
    print("invalid number ")
    print("only digits are allowed....")
except ZeroDivisionError:
    print("2nd number must not be zero ")
print("Good bye...")
