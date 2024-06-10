
n = int(input())
counts = dict()
for _ in range(n):
    s = input()
    counts[s] = counts.get(s, 0) + 1
max_count = max(counts.values())
for k, v in sorted(counts.items()):
    if v == max_count:
        print(k)

