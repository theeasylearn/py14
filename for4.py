#vowels in given line(string) using for loop 
line = input("what is your fullname")
vowel_counter = 0
for letter in line:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U':
        vowel_counter=vowel_counter+1
print("no of vowels = ",vowel_counter)
        
