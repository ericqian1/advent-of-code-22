# Hard code time.
import time

monkeys = {0: [61], 
		   1: [76, 92, 53, 93, 79, 86, 81],
		   2: [91, 99],
		   3: [58, 67, 66],
		   4: [94, 54, 62, 73], 
		   5: [59, 95, 51, 58, 58],
		   6: [87, 69, 92, 56, 91, 93, 88, 73],
		   7: [71, 57, 86, 67, 96, 95]}

worry = {0: lambda x: x*11,
		 1: lambda x: x+4,
		 2: lambda x: x*19,
		 3: lambda x: x*x,
		 4: lambda x: x+1,
		 5: lambda x: x+3,
		 6: lambda x: x+8,
		 7: lambda x: x+7}		   

def assign(worry, moduli,i, j):
	return i if worry%moduli==0 else j 

links = {0: lambda x: assign(x, 5, 7, 4),
		 1: lambda x: assign(x, 2, 2, 6),
		 2: lambda x: assign(x, 13, 5, 0),
		 3: lambda x: assign(x, 7, 6, 1),
		 4: lambda x: assign(x, 19, 3, 7),
		 5: lambda x: assign(x, 11, 0, 4),
		 6: lambda x: assign(x, 3, 5, 2),
		 7: lambda x: assign(x, 17, 3, 1)}


monkey_business = {i: 0 for i in range(8)}

for round in range(20):
	for monkey, items in monkeys.items():
		while items:
			item = items.pop(0)
			monkey_business[monkey] += 1
			new_item = int(worry[monkey](item)/3)
			monkeys[links[monkey](new_item)].append(new_item)

print(monkey_business)

# 276 * 278	

# Part 2: WTF
monkeys = {0: [61], 
		   1: [76, 92, 53, 93, 79, 86, 81],
		   2: [91, 99],
		   3: [58, 67, 66],
		   4: [94, 54, 62, 73], 
		   5: [59, 95, 51, 58, 58],
		   6: [87, 69, 92, 56, 91, 93, 88, 73],
		   7: [71, 57, 86, 67, 96, 95]}

def assign(worry, moduli,i, j):
	return i if worry[moduli]==0 else j 

links = {0: lambda x: assign(x, 5, 7, 4),
		 1: lambda x: assign(x, 2, 2, 6),
		 2: lambda x: assign(x, 13, 5, 0),
		 3: lambda x: assign(x, 7, 6, 1),
		 4: lambda x: assign(x, 19, 3, 7),
		 5: lambda x: assign(x, 11, 0, 4),
		 6: lambda x: assign(x, 3, 5, 2),
		 7: lambda x: assign(x, 17, 3, 1)}

moduli = [2,3,5,7,11,13,17,19]
monkey_mod = {monkey: [{mod: item%mod for mod in moduli} for item in items] for monkey, items in monkeys.items()}

monkey_business = {i: 0 for i in range(8)}

for round in range(10000):
	for monkey, moduli in monkey_mod.items():
		while moduli:
			factors = moduli.pop(0)
			monkey_business[monkey] += 1
			new_factors = {mod: worry[monkey](factor)%mod for mod, factor in factors.items()}
			monkey_mod[links[monkey](new_factors)].append(new_factors)


print(monkey_business)

