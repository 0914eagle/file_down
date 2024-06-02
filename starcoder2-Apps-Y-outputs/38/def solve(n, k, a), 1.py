
def solve(n, k, a):
    a.sort()
    ans = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] <= 5:
            ans += 2
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))


def solve(n, s):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if s[i:j] == s[i:j][::-1]:
                ans += 1
    return ans

n = int(input())
s = input()
print(solve(n, s))

