#concept of list 
fruits = ['apple','banana','mango','pinapple','kiwi'] #string 
list = [100,12.7,True,'the easylearn academy'] #mixed type
print(fruits)
print(list)
print(fruits[0]) #will print first fruit 
print(fruits[0:3]) #will print first 3 fruits
print(fruits[3:]) #all fruits 3rd position onwards
print(fruits + list)
mixed = fruits + list #it create new list which has both fruits and list values 
print(mixed)
fruits[0] = "water melon"
del fruits[1] #delete item from given position
print(fruits)
vegitables =  [] #empty list
print(vegitables)