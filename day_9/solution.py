import time

def conduct_move(h, direc):
	# Conduct the move
	if direc=="U":
		h[0]+=1
	elif direc=="D":
		h[0]-=1
	elif direc=="L":
		h[1]-=1
	elif direc=="R":
		h[1]+=1
	return h


h = [0,0]
t = [0,0]
moves = []
# Just a trick to catch values
dict_vals = {tuple(t): 1}
with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\t").strip("\n")
		commands = line.split(" ")
		direc, moves = commands[0], commands[1]
		for move in range(int(moves)):
			print(line, h, t)

			# Conduct the move
			h = conduct_move(h, direc)

			delta_x = abs(h[1] - t[1])
			delta_y = abs(h[0] - t[0])
			if delta_x == 2 or delta_y == 2:
				t = conduct_move(t, direc)

				if delta_y==1:
					t[0] = h[0]
				if delta_x==1:
					t[1] = h[1]	
			dict_vals[tuple(t)] = 1

print(len(dict_vals))

# Part 2: Extend the problem to go over a series of rope, its Markovian so basically just compare two at a time 

knots = [[0,0] for _ in range(10)]


dict_vals = {tuple(knots[-1]): 1}
with open("data.txt") as f:
	for line in f.readlines():
		line = line.strip("\t").strip("\n")
		commands = line.split(" ")
		direc, moves = commands[0], commands[1]
		for move in range(int(moves)):
			print(line, knots)
			knots[0] = conduct_move(knots[0], direc)
			for i in range(1, len(knots)):

				# Conduct the moves
				delta_x = knots[i-1][1] - knots[i][1]
				delta_y = knots[i-1][0] - knots[i][0]
				# Ended up having to generalize this portion
				if abs(delta_x) == 2:
					knots[i][1] = knots[i][1]+int(delta_x/2)
					if abs(delta_y)==1:
						knots[i][0] += delta_y
				if abs(delta_y) == 2:
					knots[i][0] = knots[i][0]+int(delta_y/2)			
					if abs(delta_x)==1:
						knots[i][1] += delta_x
			dict_vals[tuple(knots[-1])] = 1
print(len(dict_vals))

