
def solve(n, k, a):
    a.sort()
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] - a[i] > 5:
                break
            res = max(res, j - i + 1)
    return res

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

