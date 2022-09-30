#write a program to findout power of given base and exponent using loop  
# base = 2, exponent = 5 power 32
# process 2 x 2 x 2 x 2 x 2 = 32
# base = 3, exponent = 4 power 81
# process 3 x 3 x 3 x 3  = 81

base = int(input("Enter base"))
exponent = int(input("Enter exponent"))

power = base #2 
count=1
while count<exponent:
    power = power * base #4
    count = count + 1
print(power)