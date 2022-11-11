#String related library functions
name = input("Enter your name")
print("original name ",name)
print("name in lowercase ",name.lower())
print("name in uppercase ",name.upper())
print("original name ",name)
if name.islower()==True:
    print(f"{name} is in lowercase")

if name.isupper()==True:
    print(f"{name} is in uppercase")
    
if name.isalnum()==True:
    print(f"{name} is alpha numeric")

if name.istitle()==True:
    print(f"{name} is in title case")
    
if name.isdigit()==True:
    print(f"{name} has only digits ")

if name.isspace()==True:
    print(f"{name} has only space")