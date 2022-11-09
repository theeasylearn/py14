import random
#generate random number between 0 and 1 
print(random.random())

#generate random float number between 10 to 99
print(random.uniform(10,99))

#generate random integer number between 10 to 99
print(random.randint(10,99))

#generate random integer number between 10 to 99 with gap
print(random.randrange(10,99,5))

colors = ['red','green','blue','yellow']
print(colors)
print(random.sample(colors,k=4))
print(random.choice(colors))
print(random.choices(colors,k=2))
random.shuffle(colors)
print(colors)
