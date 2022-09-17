#concept of dictionary methods
list = ['name','surname','gender','age','weight']
print(list)

# create dictionary using list 
person = dict.fromkeys(list)
print(person)
#let us update value 
person['name'] = "Ankit"
person['surname'] = "Patel"
person['gender'] = True

print(person)

# how to get value from dictionary
print("name ",person['name'])
print("surname ",person['surname'])
# print("pincode ",person['pincode'])

#how to get value from dictionary using get method 
print("Gender", person.get("gender","not found"))
print("pincode", person.get("pincode","not found"))

#get all keys from dictionary
allkeys = person.keys()

print(allkeys)

#get all values from dictionary
allvalues = person.values()
print(allvalues)

#remove key from dictionary if exists 
response = person.pop("weight","Not Found")
print(response)
print(person)

response2 = person.pop("email","Not Found")
print(response2)

removed_item = person.popitem()
print(removed_item)
education = {"qulification":"mca","name":"Ankit M Patel"}
print(education)

person.update(education)
print(person)
