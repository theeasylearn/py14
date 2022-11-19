#write a program to create file in python and write content into file 
FileName = input("Enter file to add new content in it")
Mode = "a" # append 
try:
    file = open(FileName,Mode)
    FileContent = input("write some text to be written into file")
    file.write(FileContent)
    file.close()
    print("File created successfully")
except FileNotFoundError:
    print("no such directory exist given in file name")
except PermissionError:
    print("you dont have permission to create file at this location")