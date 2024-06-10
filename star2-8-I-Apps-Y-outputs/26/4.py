
import sys
def change(s, k):
    n = len(s)
    if n <= k:
        return 0
    if k == 1:
        return 1
    rgb = {'R':0, 'G':1, 'B':2}
    s = [rgb[c] for c in s]
    r = [(s[i] - i) % 3 for i in range(n)]
    res = 0
    for i in range(k):
        if s[i] != r[i]:
            res += 1
    return res
q = int(sys.stdin.readline())
for _ in range(q):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()
    print(change(s, k))

