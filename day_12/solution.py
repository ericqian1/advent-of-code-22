import numpy as np
import time
import pandas as pd

arr = []
char_to_int = {char: val for val, char in enumerate("abcdefghijklmnopqrstuvwxyz")}

# Part 1: Djykstra
with open("data.txt") as f:
	for i, line in enumerate(f.readlines()):
		line = line.strip("\n").strip("\t")
		in_arr = []
		for j, char in enumerate(line):
			if char=="S":
				char="a"
				start = (i, j)
			elif char=="E":
				end = (i, j)
				char="z"
			in_arr.append(char_to_int[char])
		arr.append(in_arr)

arr = np.array(arr)

vertices = {}
dims = arr.shape
for index, x in np.ndenumerate(arr):
	vertices[index] = []
	i,j = index
	adjs = [(i-1,j), (i+1,j), (i,j+1), (i,j-1)]
	for adj in adjs:
		i_2, j_2 = adj
		if 0<=i_2<dims[0] and 0<=j_2<dims[1]:
			if arr[i_2, j_2]-x<=1:
				vertices[index].append(tuple(adj))

dists = {v: 999 for v in vertices.keys()}
dists[start] = 0

to_visit = [start]
dist_cache = [dists[start]]
visited = []

while to_visit:
	vertex, distance = to_visit.pop(0), dist_cache.pop(0)
	visited.append(vertex)
	for target in vertices[vertex]:
		if target not in visited:
			dist = 1+dists[vertex]
			if dist < dists[target]:
				dists[target] = dist
				if target not in to_visit:
					to_visit.append(target)
					dist_cache.append(dists[target])
					to_visit = [x for _,x in sorted(zip(dist_cache, to_visit))]
					dist_cache = sorted(dist_cache)

print(dists[end])

# Part 2: Invert
min_dist_abs = 99999
for index, x in np.ndenumerate(arr):
	if x==0:
		start = index
		print(start)
		dists = {v: 999 for v in vertices.keys()}
		dists[start] = 0

		to_visit = [start]
		dist_cache = [dists[start]]
		visited = []

		while to_visit:
			vertex, distance = to_visit.pop(0), dist_cache.pop(0)
			visited.append(vertex)
			for target in vertices[vertex]:
				if target not in visited:
					dist = 1+dists[vertex]
					if dist < dists[target]:
						dists[target] = dist
						if target not in to_visit:
							to_visit.append(target)
							dist_cache.append(dists[target])
							to_visit = [x for _,x in sorted(zip(dist_cache, to_visit))]
							dist_cache = sorted(dist_cache)
		print(dists[end])
		if dists[end]<min_dist_abs:
			min_dist_abs = dists[end]
print(min_dist_abs)