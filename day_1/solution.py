from datetime import datetime

## Part 1
with open("data.txt") as f:
    max_total = 0
    current_total = 0
    for line in f.readlines():
        try:
            current_total += int(line)
        except:
            max_total = current_total if max_total < current_total else max_total
            current_total = 0

## Part 2 
now = datetime.now()

top_three = [0,0,0]
with open("data.txt") as f:
    max_total = 0
    current_total = 0
    new_idx = -1
    for line in f.readlines():
        try:
            current_total += int(line)
        except:
            for idx in range(len(top_three)):
                if current_total > top_three[idx]:
                    new_idx = idx
            # Avoid sorting functions by using a sorted array
            if new_idx==-1:
                pass
            else:
                top_three.insert(new_idx+1, current_total)
                del top_three[0]
            current_total = 0
            new_idx = -1
