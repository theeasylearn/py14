'''
1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5
'''
row = 1
while row<=5: #outer loop
    column=1
    while column<=row: #inner loop
        print(column,end=' ')
        column=column+1
    print("")
    row=row+1
