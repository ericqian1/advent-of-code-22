import ast

lines = []
with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\n").strip("\t")
		if "[" in line:
			lines.append(ast.literal_eval(line))


def check(left, right):
	
	finish = None

	if type(left)!=type(right):
		if type(left)==int:
			left = [left]
		if type(right)==int:
			right = [right]

	if type(left)==int and type(right)==int:
		if left==right:
			return
		elif left<right:
			return True
		else:
			return False

	if len(left)==0 and len(right)>0:
		return True
	elif len(left)>=0 and len(right)==0:
		return False

	while left and right:
		left_el = left.pop(0)
		right_el = right.pop(0)
		return check(left_el, right_el)


n_lines = len(lines)/2
count = 0
for i in range(int(n_lines)):
	left = lines[(i)*2]
	right = lines[(i*2)+1]
	if check(left, right):
		count += 1

print(count)