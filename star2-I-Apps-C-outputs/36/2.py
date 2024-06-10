
def solve(s, t):
    pos = -1
    for i in range(len(s)):
        if s[i] == "*":
            pos = i
            break
    
    if pos == -1:
        return s == t
    
    if len(s) - 1 == pos:
        return s[:-1] == t[:len(s) - 1]
    
    return t.find(s[:pos]) != -1 and t.rfind(s[pos + 1:]) == len(t) - len(s) + pos + 1

n, m = map(int, input().split())
s = input()
t = input()
if solve(s, t):
    print("YES")
else:
    print("NO")

