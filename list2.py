#concept of list 
fruits = ['apple','banana','mango','kiwi','pinapple','kiwi'] #string 
print(fruits)
#add new item at the end of list 
fruits.append('water melon')
fruits.append('cherry')
print(fruits)
#insert at begining
fruits.insert(0,'graps')
print(fruits)
fruits.insert(1,'coconut')
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.pop(2)
print(fruits)
position = fruits.index("cherry")
print("position of cherry ",position)
count = fruits.count("kiwi")
print('count of kiwi',count)
fruits.clear()
print(fruits)