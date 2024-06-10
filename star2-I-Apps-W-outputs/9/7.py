
def search(t, s):
    n, m = len(t), len(s)
    res = 0
    for i in range(n - m + 1):
        if t[i:i + m] == s:
            res += 1
    return res


n, m = map(int, input().split())
t = input().split()
s = input().split()
t = "".join([c * int(l) for l, c in t])
s = "".join([c * int(l) for l, c in s])
print(search(t, s))

