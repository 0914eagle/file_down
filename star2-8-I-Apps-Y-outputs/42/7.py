
votes = dict()
while True:
    name = input()
    if name == '***':
        break
    if name not in votes:
        votes[name] = 1
    else:
        votes[name] += 1

max_votes = max(votes.values())
if max_votes > sum(votes.values()) // 2:
    print(max(votes, key=votes.get))
else:
    print('Runoff!')

