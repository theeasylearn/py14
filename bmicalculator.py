# write a program to findout BMI of user using given height(foot,inch) and given weight
print("Enter your height in foot and inch")
foot = input("enter foot of your height")
inch = input("enter remaining inches of your height")
weight = input("enter your weight in kg")
foot = int(foot)
inch = int(inch)
weight = int(weight)
total_inch = (foot * 12) + inch
meter = total_inch / 39.37
bmi = weight / (meter * meter)
print("your bmi is",bmi)