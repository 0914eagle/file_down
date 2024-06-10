
n = int(input())
a = [int(i) for i in input().split()]
seen = {}
res = []
for i in range(n-1, -1, -1):
    if a[i] in seen:
        continue
    seen[a[i]] = True
    res.append(a[i])
print(len(res))
print(' '.join([str(i) for i in res[::-1]]))

