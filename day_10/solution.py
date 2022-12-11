import numpy as np

# Part 1 is pretty straightforward
with open("data.txt") as f:
	cycle = 0
	mov = 0
	interest = [20, 60, 100, 140, 180, 220]
	solution = []
	prev_mov = 0
	X = 1	

	for line in f.readlines():
		line = line.strip("\n").strip("\t")

		commands = line.split(" ")
		ticks = 1 if commands[0]=="noop" else 2

		next_mov = 0 if ticks==1 else int(commands[1])

		for tick in range(ticks):
			X += prev_mov
			prev_mov = 0
			cycle += 1
			if cycle in interest:
				solution.append(cycle*X)
			print(commands, cycle, X)
		prev_mov = next_mov 

print(sum(solution))

# Part 2
with open("data.txt") as f:
	pixels = []
	cycle = 0
	mov = 0
	sprite = np.array([0,1,2])
	solution = []
	prev_mov = 0
	X = 1	

	for line in f.readlines():
		line = line.strip("\n").strip("\t")

		commands = line.split(" ")
		ticks = 1 if commands[0]=="noop" else 2

		next_mov = 0 if ticks==1 else int(commands[1])

		for tick in range(ticks):
			sprite += prev_mov
			prev_mov = 0
			cycle += 1
			if (cycle-1)%40 in sprite:
				pixels.append("#")
			else:
				pixels.append(".")
			print(commands, cycle, sprite)
		prev_mov = next_mov 

for x in range(6):
	print(pixels[x*40:(x+1)*40-1])

