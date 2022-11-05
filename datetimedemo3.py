#find gap between two time object 
from datetime import time 
from datetime import datetime
print("Enter start time")
hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
second = int(input("Enter second"))
StartTime = time(hour,minute,second)
print("Enter end time")
hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
second = int(input("Enter second"))
EndTime =  time(hour,minute,second)
day=datetime.today()
difference = datetime.combine(day,EndTime) - datetime.combine(day,StartTime)
print(StartTime)
print(EndTime)
print(difference)