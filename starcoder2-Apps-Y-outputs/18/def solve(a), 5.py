
def solve(a):
    n = len(a)
    res = [0] * n
    i = 0
    j = n - 1
    while i < n and j >= 0:
        if i == j:
            res[i] = 1
            break
        if a[i] < a[j]:
            res[i] = 1
            i += 1
        elif a[i] > a[j]:
            res[j] = 1
            j -= 1
        else:
            if i + 1 == j:
                res[i] = 1
                res[j] = 1
                break
            else:
                return "NO"
    return "YES\n" + " ".join(map(str, res))

n = int(input())
a = list(map(int, input().split()))
print(solve(a))

