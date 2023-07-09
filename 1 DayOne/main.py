
with open('input.in') as file:
    data = [i for i in file.read().strip().split("\n")]


#print(data)
# ananas

max = 0
max2 = 0    
max3 = 0    
count = 0
for item in data:
    if item == '':
        count = 0       
    else:
        num = int(item) 
        count += num
        if count > 67000:
            print(count)
        

    #max values
    if count > max: 
        max = count 
    elif count > max2:
        max2 = count    
    elif count > max3:
        max3 = count    

print(max + 69727 +  max2, "top 3")
print("Total calories of top 3 Elf are:", max + max2 + max3)