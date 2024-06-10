
def solve(t, s):
    n, m = len(t), len(s)
    if m > n:
        return 0
    pos = 0
    res = 0
    for i in range(n):
        if t[i] == s[pos]:
            pos += 1
            if pos == m:
                res += 1
                pos = 0
    return res

n, m = map(int, input().split())
t = input().split()
s = input().split()
t = ''.join([c * int(l) for l, c in t])
s = ''.join([c * int(l) for l, c in s])
print(solve(t, s))

