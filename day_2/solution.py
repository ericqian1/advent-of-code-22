# Choice
choice_scores = {"X": 1,
                 "Y": 2,
                 "Z": 3}

beats = {"A": "Y",
        "B": "Z",
        "C": "X"}

losses = {"A": "Z",
        "B": "X",
        "C": "Y"}

mapping = {"A": "X",
            "B": "Y",
            "C": "Z"}

total_score = 0
## Part 1
with open("data.txt") as f:
    for line in f.readlines():
        splits = line.replace("\n", "").split(" ")
        a, b = splits[0], splits[1]
        if mapping[a]==b:
            total_score += 3
        elif beats[a]==b:
            total_score += 6
        total_score += choice_scores[b]

print(total_score)

# Part 2: Invert the problem

total_score = 0
win_share = {"X":  0,
            "Y": 3,
            "Z": 6}

with open("data.txt") as f:
    for line in f.readlines():
        splits = line.replace("\n", "").split(" ")
        a, b = splits[0], splits[1]
        if b=="Z":
            total_score += choice_scores[beats[a]]
        elif b=="Y":
            total_score += choice_scores[mapping[a]]
        else:
            total_score += choice_scores[losses[a]]
        total_score += win_share[b]

print(total_score)
