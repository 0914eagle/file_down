
def solve(k, a):
    n = 7
    days = 0
    for i in range(n):
        if a[i] == 1:
            days += 1
    if days == 0:
        return -1
    res = k // days * n
    for i in range(n):
        if a[i] == 1:
            res += i + 1
            break
    return res

t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    print(solve(k, a))

