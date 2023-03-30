from datetime import datetime 
def GetDate():
    now = datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    indian_format_date = day + "/" + month + "/" + year
    return indian_format_date
def GetTime():
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    time = hour + ":" + minute + ":" + second
    return time
def ConvertToDMY(mydate):
    mydate = str(mydate.day) + "-" + str(mydate.month) + "-" + str(mydate.year);
    return mydate