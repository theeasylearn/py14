#example of keyword arguments 
#with return value with argument function
def getScienceMarit(maths,science,english,hindi,gujarati):
    print(f"maths = {maths} science = {science} english = {english} hindi = {hindi} gujarati = {gujarati}")
    total = maths + science 
    return total 

m = int(input("Enter maths mark"))
s = int(input("Enter science mark"))
e = int(input("Enter english mark"))
h = int(input("Enter hindi mark"))
g = int(input("Enter gujarati mark"))

total = getScienceMarit(english=e,hindi=h,gujarati=g,maths=m,science=s)
print(f"maths and science total = {total}")

