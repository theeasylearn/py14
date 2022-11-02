import datetime
#get current date and time 
CurrentDateTime = datetime.datetime.now()
print(CurrentDateTime)

#get current date
CurrentDate = datetime.date.today() #return date in YYYY-MM-DD
print(CurrentDate)
#GET DATE in dd-mm-yyyy
IndianDate = str(CurrentDate.day) + "-" + str(CurrentDate.month) + "-" + str(CurrentDate.year)
print(IndianDate)