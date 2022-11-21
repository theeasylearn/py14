#read data from file and write data into file 
FileReader = open("source.txt","r")
FileWriter = open("destination.txt","w")
for line in FileReader:
    print(line,end='')
    FileWriter.write(line)
FileReader.close()
FileWriter.close()