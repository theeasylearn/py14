#write a program to findout total & average of all integer value in list 
numbers = [True,False,10,20,50]
total=0
count=0
for item in numbers:
    print(item)
    try:
        if item==False or item==True:
            print(f"{item} is not a boolean so it is skiped")
        else:
            total=total + item
            count=count+1
    except TypeError:
        print(f"{item} is not a number so it is skiped")
print(count)
try:
    average = total / count
    print(total)
    print(average)
except ZeroDivisionError:
    print("Either list is empty or all values are invalid")
