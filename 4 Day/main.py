with open('input.in', 'r') as f:
    pairs = [line.replace('\n', "") for line in f.readlines()]
    
    
    # "a-b,xy" => [['a','b'],['x','y']]
    pairs = [
        [
            [
                int(x)
                for x in elf.split('-')
            ]
            for elf in pair.split(",")
        ]
        for pair in pairs
    ]
    
total = 0
for pair in pairs:
    if(pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])\
    or(pair[1][0]<= pair[0][0] and pair[1][1] >= pair[0][1]):
        total +=1
        
print(f'Part1 :{total}')