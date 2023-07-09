import re
import copy

crates = []
with open("input.in") as fh:
    line = fh.readline()
    while line != '\n':
        crates.append(line)
        line = fh.readline()


    stackid = [int(x) for x in crates[-1].split()]

    stacks = list([] for _ in range(stackid[-1] + 1))
    for h in crates[:-1]:
        for id in stackid:
            crate = h[4 * (id - 1) + 1]
            if crate != ' ':
                stacks[id].append(crate)

    rearrangement = [[int(x) for x in re.findall("\d+", line)] for line in fh.readlines()]


stacks_copy = copy.deepcopy(stacks)

def simulate(stacks, rearrangement, m, old_crane=True):
    for n,f,t in rearrangement:
        if old_crane:
            stacks[t][0:0] = stacks[f][:n][::-1]
        else:
            stacks[t][0:0] = stacks[f][:n]
        stacks[f] = stacks[f][n:]

    return ''.join([stacks[i][0] for i in range(1, m + 1)])


print(simulate(stacks, rearrangement, len(stackid)))

print(simulate(stacks_copy, rearrangement, len(stackid), old_crane=False))