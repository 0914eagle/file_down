
N = int(input())
S = [input() for _ in range(N)]
max_count = max([S.count(s) for s in set(S)])
print(*sorted([s for s in set(S) if S.count(s) == max_count]), sep="\n")

