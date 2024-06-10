
n, m = map(int, input().split())
s = input()
t = input()

def match(s, t, i, j):
    if i == len(s) and j == len(t):
        return True
    if i == len(s) or j == len(t):
        return False
    
    if s[i] == "*":
        return match(s, t, i + 1, j) or match(s, t, i + 1, j + 1)
    else:
        return s[i] == t[j] and match(s, t, i + 1, j + 1)

print("YES" if match(s, t, 0, 0) else "NO")

