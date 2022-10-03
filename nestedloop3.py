'''
1 2 1 2 1
1 2 1 2
1 2 1
1 2 
1
'''
column = 5
while column>=1:
    row = 1
    while row<=column: 
        reminder = row%2 #1
        if reminder==1:
            print("1",end=' ')
        else:
            print("2",end=' ')
        row = row + 1
    print("")
    column = column - 1