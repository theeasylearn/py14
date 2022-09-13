#concept of dictionary 
#create dictionary
person = {"fullname":"Ankit Patel","age":38,"weight":75.11,"gender":True,"secret":123123}
print(person)
person['city'] = "Bhavnagar" #it will add new key into dictionary
person['pincode'] = 364002 #it will add new key into dictionary
print(person)
person['weight'] = 74.99
print(person)
del person['secret'] #it will delete secret key and its value
print(person)
del person #it will delete whole dictionary
# print(person)