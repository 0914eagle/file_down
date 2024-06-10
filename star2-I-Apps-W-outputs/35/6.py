
def solve(k, a):
    if sum(a) == 0:
        return -1
    res = 0
    for i in range(7):
        if a[i] == 1:
            res += k
            break
    return res

t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    print(solve(k, a))

