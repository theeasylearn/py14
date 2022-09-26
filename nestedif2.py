#write a program to findout whether given year is leap year or not 
#year = 2020 output it is leap year
#year = 2021 output it is not leap year 

year = int(input("Enter year")) #2000
reminder1 = year % 4 #0
reminder2 = year % 100 #0
reminder3 = year % 400 #0
if reminder1==0 and reminder2!=0:
    print(f"{year} is leap year")
else:
    if reminder2==0 and reminder3==0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
    