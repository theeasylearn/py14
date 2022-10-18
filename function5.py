def GetVolume(length,width=1,height=1):
    temp = length * width * height 
    return temp 

length = int(input("Enter length"))
width = int(input("Enter width"))
height = int(input("Enter height"))

volume = GetVolume(length)
print(f"Volume = {volume}")

volume = GetVolume(length,width)
print(f"Volume = {volume}")

volume = GetVolume(length,width,height)
print(f"Volume = {volume}")
