
from collections import defaultdict

def count_vote():
    votes = defaultdict(int)
    while True:
        candidate = input()
        if candidate == '***':
            break
        votes[candidate] += 1
    max_votes = max(votes.values())
    if max_votes > sum(votes.values()) / 2:
        return max(votes, key=lambda k: votes[k])
    return 'Runoff!'

print(count_vote())

