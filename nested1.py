#example of nested decision making statement
#write a program to findout largest shape from 3 shapes given length and width.

length1 = int(input("Enter length of first shape"))
width1 = int(input("Enter width  of first shape"))

length2 = int(input("Enter length of second shape"))
width2 = int(input("Enter width  of second shape"))

length3 = int(input("Enter length of third shape"))
width3 = int(input("Enter width  of third shape"))

area1 = length1 * width1
area2 = length2 * width2
area3 = length3 * width3

print(f"first shape area = {area1} second shape area = {area2} third shape area = {area3} ")

if area1>area2:
    if area1>area3:
        print("first shape is the largest shape")
    else:
        print("third shape is the largest shape")    
else:
    if area2>area3:
        print("second shape is the largest shape")
    else:
        print("third shape is the largest shape")  