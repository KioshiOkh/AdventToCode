
input = [line.split() for line in open("input.in", "r").read().splitlines()]

X = 1
cycle = 1
crt_num = 0

signalstarke: list[int] = []
pixels: str = ""

def do_cycle():
    global crt_num
    global pixels
    
    if (cycle - 20) % 40 == 0:
        signalstarke.append(cycle * X)
    
    pixels += "🧊" if X - 1 <= crt_num <= X + 1 else "⭕"
    crt_num += 1 if crt_num < 39 else -39
    
    if crt_num == 0:
        pixels += "\n"
    return 1

for i in input:
    cycle += do_cycle()
    
    if i[0] == "addx":
        cycle += do_cycle()
        X += int(i[1])

print(f"SOLUTION: {sum(signalstarke)}")
print(f"SOLUTION TWO: \n{pixels}")