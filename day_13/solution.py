import ast
import time 
import copy

# Part 1
lines = []
with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\n").strip("\t")
		if "[" in line:
			lines.append(ast.literal_eval(line))


def check(left, right):
	
	if type(left)==int and type(right)==int:
		if left==right:
			return None
		elif left<right:
			return True
		else:
			return False

	if type(left)!=type(right):
		if type(left)==int:
			left = [left]
		if type(right)==int:
			right = [right]

	if type(left)==list and type(right)==list:
		if len(left)==0 and len(right)>0:
			return True
		elif len(left)>0 and len(right)==0:
			return False
		elif len(left)==0 and len(right)==0:
			return None
		finish = check(left[0], right[0])
		if finish is None:
			return check(left[1:], right[1:])
		else:
			return finish 


n_lines = len(lines)/2
count = []
not_count = []
for idx, i in enumerate(range(int(n_lines))):
	left = lines[(i)*2]
	right = lines[(i*2)+1]
	test = check(copy.deepcopy(left), copy.deepcopy(right))
	if test:
		count.append(idx+1)
	else:
		not_count.append(idx+1)

# Part 2
lines_2 = copy.deepcopy(lines)
lines_2.append([[2]])
lines_2.append([[6]])

# Some bad sorting algorithm
keep_checking = True
sorts = 0
swaps = 0
while keep_checking:
	sorts += 1
	keep_checking = False
	swaps = 0
	for i in range(1, len(lines_2)):
		left = copy.deepcopy(lines_2[i-1])
		right = copy.deepcopy(lines_2[i])
		test = check(copy.deepcopy(left), copy.deepcopy(right))
		if not test:
			# Swap
			lines_2[i-1] = right
			lines_2[i] = left
			keep_checking = True
			swaps+=1
	print(sorts, swaps)

print(lines_2.index([[2]])+1, lines_2.index([[6]])+1)
