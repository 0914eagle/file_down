
n = int(input())
votes = {}
for _ in range(n):
    s = input()
    votes[s] = votes.get(s, 0) + 1
max_count = max(votes.values())
for s, count in sorted(votes.items()):
    if count == max_count:
        print(s)

