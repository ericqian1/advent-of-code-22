

# part 1
count = 0
with open("data.txt") as f:
	for line in f.readlines():
		pair = line.strip("\n").strip("\t")
		pair = pair.split(",")
		r_1, r_2 = pair[0].split("-"), pair[1].split("-")
		if (int(r_1[0]) >= int(r_2[0])) and (int(r_1[1]) <= int(r_2[1])) \
		or (int(r_1[0]) <= int(r_2[0])) and (int(r_1[1]) >= int(r_2[1])):
			count += 1

print(count)

# part 2
count = 0
with open("data.txt") as f:
	for line in f.readlines():
		pair = line.strip("\n").strip("\t")
		pair = pair.split(",")
		r_1, r_2 = pair[0].split("-"), pair[1].split("-")
		for i in range(int(r_1[0]), int(r_1[1])+1):
			if int(r_2[0]) <= i <= int(r_2[1]):
				count += 1
				break

print(count)
