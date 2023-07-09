sections = [ [list(map(int, s.split("-"))) for s in line.split(",")] for line in open("input.in").read().splitlines()]
overlap = sum([a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d for(a,b),(c,d) in sections])
print(overlap)