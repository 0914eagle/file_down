
import sys
votes = {}
for line in sys.stdin:
    line = line.strip()
    if line == "***":
        break
    if line not in votes:
        votes[line] = 1
    else:
        votes[line] += 1
max_votes = max(votes.values())
if list(votes.values()).count(max_votes) == 1:
    print(max(votes, key=lambda x: votes[x]))
else:
    print("Runoff!")

