#find gap between two time object 
from datetime import time 

print("Enter start time")

hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
second = int(input("Enter second"))
StartTime = time(hour,minute,second)

print("Enter end time")
hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
second = int(input("Enter second"))
EndTime = time(hour,minute,second)

# Difference = EndTime.Sub(StartTime)
# print("Difference",Difference)

print(StartTime)
print(EndTime)