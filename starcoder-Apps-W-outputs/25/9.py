
# with python3
# read input
n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = []
for i in range(m):
    b.append([int(i) for i in input().split()])

# process
res = []
for i in range(n):
    res.append(0)
    for j in range(m):
        if b[j][0] <= a[i]:
            res[i] += b[j][1]

# print output
for i in range(n):
    print(res[i], end=' ')
