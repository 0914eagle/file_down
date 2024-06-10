
def solve(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] or s[i] == "*":
            i += 1
            j += 1
        else:
            return False
    return i == len(s)

n, m = map(int, input().split())
s = input()
t = input()
if solve(s, t):
    print("YES")
else:
    print("NO")

