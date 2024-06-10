
N = int(input())
votes = {}
for _ in range(N):
    s = input()
    votes[s] = votes.get(s, 0) + 1
max_votes = max(votes.values())
for s, n in votes.items():
    if n == max_votes:
        print(s)

