#write a program to count odd and even values in list 
numbers = [1,2,3,4,5,6,10]
odd = 0 #integer
even = 0 #integer 
for item in numbers:
    reminder = item % 2
    if reminder==0:
        even = even + 1
    else:
        odd = odd + 1

print("odd = ",odd)
print("even = ",even)