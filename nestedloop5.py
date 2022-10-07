#write a program to findout armstring no between 1 to 10000
import math
count = 1
while count<=10000:
    number = count
    copy_number = number
    total=0
    size = len(str(number)) #3
    # print(size)
    #number = 153

    while number>0:
        reminder = number % 10 #3
        result = int(math.pow(reminder,size))
        total=total+result # 27
        number = number // 10

    if total==copy_number:
        print(copy_number)
    count=count+1

