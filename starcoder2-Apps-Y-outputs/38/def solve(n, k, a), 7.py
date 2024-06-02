
def solve(n, k, a):
    a.sort()
    ans = 0
    for i in range(n):
        if i + k - 1 >= n:
            break
        ans = max(ans, sum(a[i + k - 1 : i + k]) - a[i])
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

