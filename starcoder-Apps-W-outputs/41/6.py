
n, m = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
print(min(d.values()))
