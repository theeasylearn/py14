#concept of set in python 
countries = {'India','usa','uk','canada','India'}
print(countries)

#let us add new value
countries.add('Russia')
countries.add('Japan')
print(countries)
countries.remove('canada')
print(countries)
# countries[0] = 'Bharat' will give error because we can not remove value of set
print(countries)
