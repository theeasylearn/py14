import os 
CurrentFileName = input('Enter Current Filename')
NewFileName = input('Enter new Filename')
os.rename(CurrentFileName,NewFileName)
print("File renamed sucessfully")