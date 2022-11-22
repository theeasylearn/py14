import os 
choice = int(input('''Press 1 to create new directory 
Press 2 to delete existing directory
Press 3 to get current working directory
Press 4 to change current working directory
Press 0 to exit 
'''))
print(choice)
if choice==1:
    NewDirectoryName = input("Enter new directory name")
    os.mkdir(NewDirectoryName)
    print(f"{NewDirectoryName} has been created successfully")
elif choice==2:
    ExistingDirectoryName = input("Enter diretory name to delete")
    os.rmdir(ExistingDirectoryName)
    print(f"{ExistingDirectoryName} has been deleted successfully")
elif choice==3:
    print("Current directory name ", os.getcwd())
elif choice==4:
    DirectoryName = input("Enter directory Name to set as current working directory")
    os.chdir(DirectoryName)
    print("Current directory name ", os.getcwd())
