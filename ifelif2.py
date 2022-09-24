#2nd example of if elif else decision making statement
'''
    write a program to findout whether given letter is vowel or consonsent.
    a e i o u theses are called vowels 
'''
letter = input("enter any one letter")
letter = letter[0]
print(f"you have pressed {letter}")
if letter=='u' or letter=='U':
    print("it is u and it is vowel")
elif letter=='e' or letter=='E':
    print("it is e and it is vowel")
elif letter=='i' or letter=='I':
    print("it is i and it is vowel")
elif letter=='o' or letter=='O':
    print("it is o and it is vowel")
elif  letter=='a' or letter=='A':
    print("it is a and it is vowel")
else:
    print("it is not vowel and it can be consonsent.")

print("have good day")
