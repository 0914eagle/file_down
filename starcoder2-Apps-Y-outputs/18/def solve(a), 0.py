
def solve(a):
    n = len(a)
    res = [0] * n
    if n == 1:
        return res
    if a[0] < a[1]:
        res[0] = 1
    for i in range(1, n - 1):
        if a[i] < a[i - 1] and a[i] < a[i + 1]:
            res[i] = 1
        elif a[i] > a[i - 1] and a[i] > a[i + 1]:
            res[i] = 0
        else:
            return "NO"
    if a[-1] < a[-2]:
        res[-1] = 1
    return res

n = int(input())
a = list(map(int, input().split()))
res = solve(a)
if res == "NO":
    print(res)
else:
    print("YES")
    print(" ".join(map(str, res)))

