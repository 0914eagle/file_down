
N = int(input())
S = [input() for _ in range(N)]
max_vote = max(S.count(s) for s in S)
for s in sorted(set(S)):
  if S.count(s) == max_vote:
    print(s)

