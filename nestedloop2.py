'''
write a program to print following pattern 
*
* *
* * *
* * * *
* * * * *
'''
line = 1
while line<=5:
    count = 1
    while count<=line:
        print('*',end=' ')
        count = count + 1
    print(" ")
    line=line + 1
