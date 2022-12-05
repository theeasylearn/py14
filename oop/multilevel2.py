# real world example of multilevel inheritance
from gbfile import GB
b = int(input("Enter bytes "))
g1 = GB(bytes = b)

kilobytes = g1.getKB()
megabytes = g1.getMB()
gigabytes = g1.getGB()

print(f"Kilobytes = {kilobytes}  megabytes = {megabytes} gigabytes = {gigabytes}")
