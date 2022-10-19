def getminmax(*values):
    min = max = values[0]
    for number in values:
        if number<min:
            min = number    
        if number>max:
            max = number
    return min,max
result = getminmax(56,5,50,-100,2,125,89)
print(result)