
# part 1: a list is an abstract stack 
stacks = [["Z", "J", "G"],
		  ["Q","L","R","P","W","F","V","C"],
		  ["F","P","M","C","L","G","R"],
		  ["F", "L", "B", "W", "P", "H", "M"],
		  ["G","C","F","S","V","Q"],
		  ["W","H","J","Z","M","Q","T","L"],
		  ["H","F","S","B","V"],
		  ["F","J","Z","S"],
		  ["M","C","D","P","F","H","B","T"]]

with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\n").strip("\t").strip("move ").replace("from ", "").replace("to ", "")
		vals = line.split(" ")
		move, from_where, to_where = int(vals[0]), int(vals[1]), int(vals[2])
		for i in range(move):
			val_out = stacks[from_where-1].pop()
			stacks[to_where-1].append(val_out)

for stack in stacks:
	print(stack[-1])

# part 2: still a stack but can grab a bunch
stacks = [["Z", "J", "G"],
		  ["Q","L","R","P","W","F","V","C"],
		  ["F","P","M","C","L","G","R"],
		  ["F", "L", "B", "W", "P", "H", "M"],
		  ["G","C","F","S","V","Q"],
		  ["W","H","J","Z","M","Q","T","L"],
		  ["H","F","S","B","V"],
		  ["F","J","Z","S"],
		  ["M","C","D","P","F","H","B","T"]]

with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\n").strip("\t").strip("move ").replace("from ", "").replace("to ", "")
		vals = line.split(" ")
		move, from_where, to_where = int(vals[0]), int(vals[1]), int(vals[2])
		len_stack = len(stacks[from_where-1])
		vals_out = stacks[from_where-1][len_stack-move:len_stack]
		stacks[from_where-1] = stacks[from_where-1][0:len_stack-move]
		stacks[to_where-1].extend(vals_out)

for stack in stacks:
	print(stack[-1])
