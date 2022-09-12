# example of tuples
gods = ('Bramha','Mahesh','Vishnu','Vishnu','Vishnu')
devtas = ('Agnidev','vayudev','varundev','indra dev','kuber','chandra dev','surya dev')
print(gods)
print(gods[1])
print(gods[0:2])
print(gods[1:])
print(devtas)
print(gods + devtas)
print("position of vishnu devtas ",gods.index('Vishnu'))
print("count of vishnu ",gods.count('Vishnu'))
del gods[0]