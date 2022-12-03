alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = {val: idx+1 for idx,val in enumerate(alphabet)}
total = 0
with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\n")
		len_line = len(line)
		bag_1 = line[0:int(len_line/2)]
		bag_2 = line[int(len_line/2):len_line]
		for char in bag_1:
			if char in bag_2:
				total+=priorities[char]
				break
print(total)
# PART 2: some clever cross multiplication trick for linear time
idx_matcher = {val: i for i, val in enumerate(alphabet)}
matrix = []
total = 0
with open("data.txt") as f:
	for idx, line in enumerate(f.readlines()):
		bag = line.strip("\n").strip("\t")
		matrix.append([0 for _ in range(len(alphabet))])
		for char in bag:
			matrix[idx%3][idx_matcher[char]] = 1

		if (idx+1)%3 == 0:
			identity = [x*y*z for x,y,z in zip(matrix[0], matrix[1], matrix[2])]
			total += identity.index(1)+1
			matrix = []

print(total)