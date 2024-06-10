
def solve(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] or s[i] == "*":
            i += 1
            j += 1
        else:
            return "NO"
    if i == len(s) and j == len(t):
        return "YES"
    elif i < len(s) and s[i] == "*":
        return "YES"
    else:
        return "NO"

n, m = map(int, input().split())
s = input()
t = input()
print(solve(s, t))

