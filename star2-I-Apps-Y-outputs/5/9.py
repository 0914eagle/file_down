
n = int(input())
x = list(map(int, input().split()))
x.sort()

def check(d):
    prev = x[0]
    for i in range(1, n):
        if x[i] - prev != d:
            return False
        prev = x[i]
    return True

l = 0
r = 2**30
while l < r:
    m = (l + r) // 2
    if check(m):
        l = m + 1
    else:
        r = m

print(n - l + 1)
print(*x[n - l:])

