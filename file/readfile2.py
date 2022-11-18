FileName = input("Enter file name to read its content ")
Mode = "r" # r = read 
try:
    file = open(FileName,Mode)
    #read content from file in single attampt
    FileContent = file.read()
    print(FileContent)
    file.close()
    print("")
except FileNotFoundError:
    print("No such file exists...")
except PermissionError:
    print("either this is not a file or you have don't permission to read file")
except UnicodeDecodeError:
    print("it is binary file therefore can not be read")
finally:
    print("End of program")
