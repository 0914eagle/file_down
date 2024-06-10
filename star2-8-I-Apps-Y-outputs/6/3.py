
n = int(input())
a = list(map(int, input().split()))
s = set()
res = []
for x in a:
    if x not in s:
        s.add(x)
        res.append(x)
print(len(res))
print(" ".join(map(str, res)))

