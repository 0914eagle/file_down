
n = int(input())
a = [int(x) for x in input().split()]
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
m = max(d.values())
for k in d:
    if d[k] == m:
        print(k)
        break

