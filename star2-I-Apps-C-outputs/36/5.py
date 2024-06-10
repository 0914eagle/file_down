
n, m = map(int, input().split())
s = input()
t = input()

def match(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        elif s[i] == "*":
            i += 1
            while j < len(t) and s[i - 1] != t[j]:
                j += 1
        else:
            return False
    return i == len(s) and j == len(t)

if match(s, t):
    print("YES")
else:
    print("NO")

