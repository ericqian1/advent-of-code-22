import numpy as np

# PART 1 
with open("data.txt") as f:
	arr = []
	for line in f.readlines():
		line = line.strip("\n").strip("\t")
		arr.append([int(i) for i in line])

arr = np.array(arr)

# Instatiate dims
row, col = arr.shape
identity = np.zeros((row, col))

# So inefficient :9
for idx in range(row):
	for idx_2 in range(col):
		if idx==0 or idx==row-1 or idx_2==0 or idx_2==col-1:
			identity[idx, idx_2] = 1
		else:
			top = np.max(arr[0:idx, idx_2])
			bottom = np.max(arr[idx+1:row, idx_2])
			left = np.max(arr[idx, 0:idx_2])
			right = np.max(arr[idx, idx_2+1:col])
			if arr[idx, idx_2] > top or arr[idx, idx_2] > bottom or arr[idx, idx_2] > left or arr[idx, idx_2] > right:
				identity[idx, idx_2] = 1


print(np.sum(identity))

# Part 2: also inefficient :(

# So inefficient :9
for idx in range(row):
	for idx_2 in range(col):
		if idx==0 or idx==row-1 or idx_2==0 or idx_2==col-1:
			identity[idx, idx_2] = 1
		else:
			val = arr[idx, idx_2]
			top = arr[0:idx, idx_2][::-1]
			bottom = arr[idx+1:row, idx_2]
			left = arr[idx, 0:idx_2][::-1]
			right = arr[idx, idx_2+1:col]	
			for i in range(len(top)):
				if val <= top[i]:
					break
			for j in range(len(bottom)):
				if val <= bottom[j]:
					break					
			for k in range(len(left)):
				if val <= left[k]:
					break
			for l in range(len(right)):
				if val <= right[l]:
					break

			identity[idx, idx_2]=(i+1)*(j+1)*(k+1)*(l+1)
print(np.max(identity))