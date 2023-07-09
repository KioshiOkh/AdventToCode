import re
with open('inputS.in') as file:
    data = [i.replace("L", "") and i.replace("R", "") for i in file.read().strip().split(", ")]

count = 0

for item in data:
    num = item
    print(num)
    count += num
print(count)