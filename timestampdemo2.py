#get current time stamp of specific date and time
from datetime import datetime 
CurrentTimestamp = datetime.now().timestamp()
print(f"Current time stamp {CurrentTimestamp}")
day = int(input("Enter day of birthdate"))
month = int(input("Enter month of birthdate"))
year = int(input("Enter year of birthdate"))

hour = int(input("Enter birth hour"))
minute = int(input("Enter birth minute"))
second = int(input("Enter birth second"))

BirthDateTime = f"{day}/{month}/{year} {hour}:{minute}:{second}"

BirthTimeStamp = datetime.strptime(BirthDateTime, "%d/%m/%Y %H:%M:%S").timestamp()
print(f"Birth time stamp {BirthTimeStamp}")

DifferenceInSeconds = int(CurrentTimestamp) - int(BirthTimeStamp)
print("Difference in seconds",DifferenceInSeconds)
print("Difference in minutes",DifferenceInSeconds/60)
print("Difference in hour",DifferenceInSeconds/(60*24))