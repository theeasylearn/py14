import datetime 
day = int(input("Enter day of birthdate"))
month = int(input("Enter month of birthdate"))
year = int(input("Enter year of birthdate"))

#construct date from given day month and year 
BirthDate = datetime.date(year,month,day)
print(BirthDate)

CurrentDate = datetime.date.today()
Difference = CurrentDate - BirthDate
print(Difference.days)
print(Difference.days/365)
