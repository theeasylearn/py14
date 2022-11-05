#calculate age of user from his birth date
from datetime import datetime
print("Enter your birth date ")
day=int(input("Enter your birth day "))
month=int(input("Enter your birth month "))
year=int(input("Enter your birth year "))
birthdate=datetime(year,month,day)
print(birthdate)
today=datetime.today()
print(today)
difference = today - birthdate
print(difference)
user_age=difference/365
print(f"user total age ={user_age.days} years")