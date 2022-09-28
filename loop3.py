# write a program to print following fibonanci pattern 
# 0 1 1 2 3 5 8 13 21 34 ....... 100

previous = 0
current = 1
next = 1

print(previous,end=' ')
print(current,end=' ')

while next<89:
    next = previous + current 
    print(next,end=' ')
    previous = current
    current = next

