
n, l, x, y = map(int, input().split())
a = list(map(int, input().split()))
add = []
for d in [x, y]:
    for i in range(n-1):
        if a[i+1] - a[i] < d:
            add.append(d - (a[i+1] - a[i]))
add.sort()
print(len(add))
print(" ".join(map(str, add)))

