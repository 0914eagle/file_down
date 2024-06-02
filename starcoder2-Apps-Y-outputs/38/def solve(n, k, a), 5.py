
def solve(n, k, a):
    a.sort()
    i = 0
    j = n - 1
    ans = 0
    while i < j:
        if a[j] - a[i] <= 5:
            ans += 2
            i += 1
            j -= 1
        else:
            ans += 1
            j -= 1
    if i == j:
        ans += 1
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

