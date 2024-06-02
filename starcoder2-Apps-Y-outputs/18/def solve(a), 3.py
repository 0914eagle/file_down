
def solve(a):
    n = len(a)
    res = [0] * n
    for i in range(n):
        if i == 0:
            res[i] = 1
        else:
            if a[i] > a[i - 1]:
                res[i] = 1
            else:
                res[i] = 0
    if res.count(0) == 0 or res.count(1) == 0:
        return "NO"
    else:
        return "YES\n" + " ".join(map(str, res))

n = int(input())
a = list(map(int, input().split()))
print(solve(a))

