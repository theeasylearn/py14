# * * * * *
#   * * * *
#     * * *
#       * *
#         *
row = 1
while row<=5:
    count = 1
    while count<row:
        print(" ",end='')
        count = count + 1
    astrik = 1
    while astrik<=6-row:
        print("*",end='')
        astrik = astrik + 1
    print("")
    row=row+1