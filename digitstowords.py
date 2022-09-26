#write a program to convert two digit amount into words 
#amount = 65 output six five 
#amount = 15 output one five 

amount = int(input("Enter amount")) #65 
if amount>99:
    print("invalid amount")
else:
    last_digit = amount % 10 #5
    # print(last_digit)
    first_digit = amount // 10
    # print(first_digit)
    if first_digit==0:
        print("zero",end=' ')
    elif first_digit==1:
        print("one",end=' ')
    elif first_digit==2:
        print("two",end=' ')
    elif first_digit==3:
        print("three",end=' ')
    elif first_digit==4:
        print("four",end=' ')
    elif first_digit==5:
        print("five",end=' ')
    elif first_digit==6:
        print("six",end=' ')
    elif first_digit==7:
        print("seven",end=' ')
    elif first_digit==8:
        print("eight",end=' ')
    elif first_digit==9:
        print("nine",end=' ')

    if last_digit==0:
        print("zero",end=' ')
    elif last_digit==1:
        print("one",end=' ')
    elif last_digit==2:
        print("two",end=' ')
    elif last_digit==3:
        print("three",end=' ')
    elif last_digit==4:
        print("four",end=' ')
    elif last_digit==5:
        print("five",end=' ')
    elif last_digit==6:
        print("six",end=' ')
    elif last_digit==7:
        print("seven",end=' ')
    elif last_digit==8:
        print("eight",end=' ')
    elif last_digit==9:
        print("nine",end=' ')