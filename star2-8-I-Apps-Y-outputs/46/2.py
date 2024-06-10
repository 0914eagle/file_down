
from collections import defaultdict
N = int(input())
votes = defaultdict(int)
for i in range(N):
    s = input()
    votes[s] += 1
max_vote = max(votes.values())
for k, v in votes.items():
    if v == max_vote:
        print(k)

