with open('input.in', 'r') as file:
    rucksacks = file.read().strip().split('\n')


priority_q1 = 0
for item in rucksacks:
    L = len(item)
    comp1 = item[:L // 2]
    comp2 = item[L // 2:]
    for item in comp1:
        if item in comp2:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26
            priority_q1 += value
            break

print('The priority for the first task is: ' + str(priority_q1))

ii = 0
priority_q2 = 0
while ii < len(rucksacks):
    bag1 = rucksacks[ii]
    bag2 = rucksacks[ii + 1]
    bag3 = rucksacks[ii + 2]
    for item in bag1:
        if item in bag2 and item in bag3:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26
            priority_q2 += value
            ii += 3
            break

print('The priority for the second task is: ' + str(priority_q2))