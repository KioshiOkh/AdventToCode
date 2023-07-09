sizes = {}
TOTAL = 0

def nested_set(dic, keys, value):
	for key in keys[:-1]:
		dic = dic.setdefault(key, {})
	dic[keys[-1]] = value

def iterdict(d):
	global sizes
	sm = 0
	for k,v in d.items():
		if isinstance(v, dict):
			sm += iterdict(v)
		else:
			sm += v
	sizes[str(d)] = sm
	return sm

with open("7.txt", "r") as inp:
	tree = {}
	ans = 0
	path = []
	for line in inp.readlines():
		token = [i.strip() for i in line.split(" ")]
		if token[1]=="cd":
			if token[2]=="..":
				path.pop()
			elif token[2]=="/":
				path = ["/"]
			else:
				path.append(token[2])
		elif token[1] == "ls":
			continue
		elif token[0] == "dir":
			nested_set(tree, path + [token[1]], {})
			continue
		else:
			nested_set(tree, path + [token[1]] , int(token[0]))
			TOTAL += int(token[0])

	iterdict(tree)


	for k,v in sizes.items():
		if v<=100000:
			ans += v
	print(ans)


	v = (sorted(list(sizes.values())))
	for size in v:
		if int(size)>=6728267:
			print(size)
			break