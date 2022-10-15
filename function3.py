#with return value without argument function 
#def function-name():
from datetime import datetime
def GetCurrentDate():
    CurrentDateTime = datetime.now()
    CurrentDate = str(CurrentDateTime.day) + "-" + str(CurrentDateTime.month) + "-" + str(CurrentDateTime.year)
    return CurrentDate
def GetCurrentTime():
    CurrentDateTime = datetime.now()
    CurrentTime = str(CurrentDateTime.hour) + ":" + str(CurrentDateTime.minute) + ":" + str(CurrentDateTime.second)
    return CurrentTime
result = GetCurrentDate()
print(result)
time = GetCurrentTime()
print(time)