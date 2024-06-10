
def solve(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] or s[i] == "*":
            i += 1
            j += 1
        elif s[i] == "*":
            i += 1
        else:
            return "NO"
    if i == len(s) and j == len(t):
        return "YES"
    elif i == len(s):
        while j < len(t):
            if t[j] != "*":
                return "NO"
            j += 1
        return "YES"
    else:
        return "NO"

n, m = map(int, input().split())
s = input()
t = input()
print(solve(s, t))

