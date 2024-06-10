
from collections import Counter

def solve(votes):
    counter = Counter(votes)
    total = len(votes)
    for candidate, count in counter.items():
        if count > total // 2:
            return candidate
    
    return "Runoff!"

votes = []
while True:
    line = input()
    if line == "***":
        break
    votes.append(line)

print(solve(votes))

