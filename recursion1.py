def GreetingMessage(count):
    print("Good Evening Students.....")
    count=count-1
    if count>=1:
        GreetingMessage(count)
    print(f"{count}")
count = 5
GreetingMessage(count)
print("Good bye...")