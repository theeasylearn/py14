# write a program  add no of days into given date to get new date
from datetime import datetime
from datetime import timedelta
print("Enter your birth date ")
day=int(input("Enter any  day "))
month=int(input("Enter any  month "))
year=int(input("Enter any  year "))
olddate=datetime(year,month,day)
print(olddate)

add_days=int(input("Enter number of days to add "))

add_days = timedelta(days=add_days)
print(add_days)
new_date = olddate+add_days
print(new_date)