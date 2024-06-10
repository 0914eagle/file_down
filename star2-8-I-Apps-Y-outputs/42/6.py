
from sys import stdin
lines = stdin.readlines()
votes = {}
for line in lines[:-1]:
    line = line.strip()
    if line in votes:
        votes[line] += 1
    else:
        votes[line] = 1
max_count = max(votes.values())
if max_count > sum(votes.values()) / 2:
    print(list(votes.keys())[list(votes.values()).index(max_count)])
else:
    print("Runoff!")

