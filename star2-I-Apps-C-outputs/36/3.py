
def solve(n, m, s, t):
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        elif s[i] == "*":
            i += 1
            while j < m and s[i - 1] != t[j]:
                j += 1
        else:
            return "NO"
    while i < n and s[i] == "*":
        i += 1
    return "YES" if i == n and j == m else "NO"

n, m = map(int, input().split())
s = input()
t = input()
print(solve(n, m, s, t))

