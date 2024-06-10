
n, a, b, c, d = map(int, input().split())

def check(x):
    return x != a and x != b and x != c and x != d

res = 0
for x in range(1, n + 1):
    if check(x):
        res += 1
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if check(x) and check(y):
            res += 1
print(res)

