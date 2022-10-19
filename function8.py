def sum(*values):
    total=0
    for number in values:
        total = total + number
    return total
result = sum(10,20,50,100,200,125,89)
print(result)