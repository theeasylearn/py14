#write a program to findout whether given year is millennium year or not 
year = int(input("enter any one year"))
reminder = year % 1000
if reminder==0:
    print("it is millennium year")
else:
    print("it is not millennium year")
    
print("Good bye....")


