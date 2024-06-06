
def longest_common_prefix(s, t):
    ans = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            ans += 1
        else:
            break
    return ans


def solve(a):
    n = len(a)
    s = [None] * (n + 1)
    s[0] = 'a' * 200
    s[1] = 'a' * (200 - a[0]) + 'b'
    for i in range(2, n):
        s[i] = s[i - 1][:len(s[i - 1]) - a[i - 1]] + 'b' * (200 - len(s[i - 1]) + a[i - 1])
    s[n] = s[n - 1][:len(s[n - 1]) - a[n - 1]] + 'b' * (200 - len(s[n - 1]) + a[n - 1])
    for i in range(1, n + 1):
        assert longest_common_prefix(s[i - 1], s[i]) == a[i - 1]
    return s


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = solve(a)
    for si in s:
        print(si)

